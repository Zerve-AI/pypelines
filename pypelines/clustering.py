#from typing import Type
import os
import pyperclip
from .templates.clustering_dataprep import ClusteringTemplate
from .schemas import HyperParamsClustering,NumericalParamClustering,CategoricalParamClustering
from .models.clustering import models_clustering,models_clustering_default,models_comparison_clustering,models_comparison_clustering_default
import pandas as pd 
from typing import Union
import inspect

clustering_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
'''

class ClusteringPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 predictions_data:Union[str, pd.DataFrame],
                 nfolds:int,
                 models:list = None):
        """
        The __init__ function is the constructor for a class.
        It initializes all of the attributes of an object, and it's called when you create a new instance of that class.
        
        
        :param self: Represent the instance of the class
        :param data:Union[str: Specify that the data parameter can be either a string or a pandas dataframe
        :param pd.DataFrame]: Pass the dataframe to the class
        :param predictions_data:Union[str: Specify the dataset that will be used for predictions
        :param pd.DataFrame]: Pass the dataframe to the class
        :param nfolds:int: Set the number of folds for cross-validation
        :param models:list: Pass a list of models to the class
        """
        
        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")
        
        if isinstance(predictions_data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            predictions_dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(predictions_data, str):
            predictions_dataset_name = predictions_data
        else:
            raise ValueError("test_data must be a pandas DataFrame or a string")

        self.dataset_name = dataset_name
        self.predictions_dataset_name = predictions_dataset_name

        if models is None:
            self.models = list(models_clustering_default.keys())
        else :
            self.models = models


        self.nfolds = nfolds
        self.models_clustering = models_clustering

    def model_list(self):
        """
        The model_list function returns a list of all the models that are available for use in the pipeline.
        :param self: Represent the instance of the class
        :return: A list of all the models
        """
        return print(self.models)

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing 
        the hyperparameter name as key and an instance of HyperParam class as value. 
        :param self: Bind the method to the class
        :return: A dictionary of hyperparameters for each model
        """
        
        self.models_ = self.models_clustering
        self.model_params = {k:v for k,v in self.models_.items() if k in self.models}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes in a model_prefix and params.
        The model_prefix is the name of the model, e.g., 'svm'. The params are all of the parameters for that particular 
        model, which includes numerical and categorical parameters. For each parameter in params, if it is selected to be searched over (i.e., search=True), then we create an instance of either NumericalParamAD or CategoricalParamAD depending on whether it's numerical or categorical respectively.
        
        :param self: Represent the instance of the class
        :param model_prefix: Prefix the name of the hyperparameter with a string
        :param params: Pass the parameters of the model
        :return: A hyperparamsad object
        """
        
        hyperparams = []
        
        for k, v in params.items():
            for p in v:
                if p.get('search')==False:
                    continue
                if k=='categorical':
                    if not p['selected']:
                        continue
                    hyperparams.append(CategoricalParamClustering(**{'prefix': model_prefix, 'name': p['name'], 'values': p['selected']}))
                elif k=='numerical':
                    hyperparams.append(NumericalParamClustering(**{'prefix': model_prefix, **p}))
        return HyperParamsClustering(**{'params': hyperparams})
    
    def parse_config(self):
        """
        The parse_config function is used to parse the configuration file and extract all of the information needed for 
        the pipeline. It extracts:
            - The dataset name, which will be used to load the data from a csv file in a directory called 'data' in your current working directory.
            - The predictions dataset name, which will be used to load predictions from a csv file in a directory called 'predictions' in your current working directory. 
            - The models that you want to run on this data (from models_clustering). This should be specified as an array of strings with each string being one model's name
        
        :param self: Refer to the object itself
        :return: A dictionary of the model parameters
        """
        
        self.models_all = models_clustering
        self.model_comp_all = models_comparison_clustering
        self.model_param = self.get_hyperparameters()
        selected_models = self.models 
        self.metric = 'silhouette_samples'
        self.default_imports = clustering_imports
        self.pipeline_params = {'dataset': self.dataset_name,'prediction_dataset':self.predictions_dataset_name}
        self.shared_model_params = {'cross_validation':self.nfolds, 'metric':self.metric }
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def generate_code(self, output_path:str=None):
        """
        The generate_code function is used to generate code for the data processing pipeline and each model.
        
        :param self: Represent the instance of the class
        :param output_path:str: Specify the path to save the generated code
        :return: The code for all models in the pipeline
        """
        
        self.parse_config()
        code_list = {}
        code_append = "" #store output for each model - used for writing code file output for each model
        code_all_models = "" #store output for all models - used for copy_to_clipboard
        code, imports, requirements = ClusteringTemplate()(self.pipeline_params)
        imports = self.default_imports + '\n' + imports
        code_append += imports
        code_append += code
        code_append += '\n'
        code_append += '\n'
        code_append += "##### End of Data Processing Pipeline #####"
        code_append += '\n'
        code_append += '\n'
        code_data_prep = code_append
        code_list['data_prep_pipeline'] = {'code':code_data_prep}
        if output_path is not None:
            output_file = open(f"{output_path}/data_prep_pipeline.py", "w")
            n = output_file.write(code_data_prep)
            output_file.close()
        code_all_models += code_data_prep
        i = 0
        for model_name, params in self.model_params.items():
            ModelTemplate= self.models_all[model_name]
            code_append = ""
            code_append = code_data_prep
            code_append += '\n'
            code_append += '\n'
            code_append += f"##### Model Pipeline for {model_name} #####"
            code_append += '\n'
            code_all_models += '\n'
            code_all_models += f"##### Model Pipeline for {model_name} #####"
            code_all_models += '\n'
            code, model_imports, model_requirements  = ModelTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelTemplate().prefix, params)
                })
            if model_requirements:
                requirements += model_requirements
            if model_imports:
                imports += '\n' + model_imports
            code_append += code
            code_all_models += code
            code_all_models += f"##### End of Model Pipeline for {model_name} #####"
            i += 1
            if len(self.model_params.items()) == i:
                ModelCompTemplate= self.model_comp_all[model_name]
                code, model_imports, model_requirements  = ModelCompTemplate()({
                    **params, 
                    **self.shared_model_params, 
                    'hyperparams': self.compile_hyperparameters(ModelCompTemplate().prefix, params)
                    })
                code_all_models += '\n'
                code_all_models += f"##### Model Comparison #####"
                code_all_models += code
                code_all_models += '\n'
            code_list[model_name] = {'code':code_append}
            if output_path is not None:
                output_file = open(f"{output_path}/{model_name}.py", "w")
                n = output_file.write(code_append)
                output_file.close()
        return code_all_models
    
    def get_code(self):
        """
        The get_code function is a method of the class CodeGenerator.
        It takes no arguments and returns the generated code as a string.
        
        :param self: Represent the instance of the class
        :return: The value of the generate_code function
        """
        code_gen = self.generate_code()
        return print(code_gen)
    
    def code_to_clipboard(self):
        """
        The code_to_clipboard function copies the generated code to the clipboard.
            
        
        :param self: Refer to the current instance of a class
        :return: The generated code is saved to clipboard
        """
        code_gen = self.generate_code()
        return pyperclip.copy(code_gen)
    
    def code_to_file(self,
                     path:str =  os.getcwd()):
        """
        The code_to_file function saves the generated code to a file.
        
        :param self: Refer to the object itself
        :param path:str: Define the path where the model files will be saved
        :return: A string indicating where the model files were saved
        """
        self.generate_code(output_path = path)
        return f'model files saved to {path}'
    
    def model_grid_search_settings(self,model_name:str=None):
        """
        The model_grid_search_settings function is used to return the hyperparameters of a model.
        
        :param self: Bind the attributes with an object
        :param model_name:str: Specify the name of the model to be used
        :return: The hyperparameters of the model
        """
        self.models_ = self.models_clustering
        self.model_params = {k:v for k,v in self.models_.items() if k in model_name}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters[name]


    def set_model_grid_search_settings(self,hyperparam_dict:dict = None, model_name:list = None, path:str=None):
        """
        The set_model_grid_search_settings function is used to manually set the model grid search settings.
        
        :param self: Represent the instance of the class
        :param hyperparam_dict:dict: Pass in a dictionary of hyperparameters to be used for the model
        :param model_name:list: Specify which models to generate code for
        :param path:str: Specify the path you want to save your code in
        :return: The code for the model pipeline
        """
        self.parse_config()
        code_append = ""
        code, imports, requirements = ClusteringTemplate()(self.pipeline_params)
        imports = self.default_imports + '\n' + imports
        code_append += imports
        code_append += code
        code_append += '\n'
        code_append += '\n'
        code_append += "##### End of Data Processing Pipeline #####"
        code_append += '\n'
        code_append += '\n'
        for model_name, params in self.model_params.items():
            ModelTemplate= self.models_all[model_name]
            code_append += '\n'
            code_append += '\n'
            code_append += f"##### Model Pipeline for {model_name} #####"
            code_append += '\n'
            code, model_imports, model_requirements  = ModelTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelTemplate().prefix, hyperparam_dict)
                })
            if model_requirements:
                requirements += model_requirements
            if model_imports:
                imports += '\n' + model_imports
            code_append += code
            ModelCompTemplate= self.model_comp_all[model_name]
            code, model_imports, model_requirements  = ModelCompTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelCompTemplate().prefix, hyperparam_dict)
                })
            code_append += f"##### Model Metrics {model_name} #####"
            code_append += code
            code_append += '\n'
            code_append += f"##### End of Model Pipeline for {model_name} #####"
            if path is not None:
                output_file = open(f"{path}/{model_name}.py", "w")
                n = output_file.write(code_append)
                output_file.close()
            pyperclip.copy(code_append)
        return print(code_append)
    