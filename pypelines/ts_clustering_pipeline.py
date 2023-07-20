import os
import pyperclip
from .templates.ts_clustering_dataprep import TSClusteringTemplate
from .schemas import HyperParamsTSClustering, NumericalParamTSClustering, CategoricalParamTSClustering
from .models.timeseries_clustering import models_ts_clustering, models_comparison_ts_clustering, models_ts_clustering_default,models_comparison_ts_clustering_default
import pandas as pd 
from typing import Union
import inspect


tsclustering_imports = '''
from sktime import *
'''

class TSClusteringPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 nfolds:int=3,
                 models:list = None):
        """
        The __init__ function initializes the class with the following parameters:

        :param self: Represent the instance of the class
        :param data:Union[str: Check if the data is a string or not
        :param pd.DataFrame]: Store the dataframe passed to the class
        :param test_data:Union[str: Specify the test data
        :param pd.DataFrame]: Pass the dataframe
        :param models:list: Pass the list of models to be trained and tested
        :param target_column:str: Specify the target column in the dataframe
        :param nfolds:int: Specify the number of folds for cross validation
        :return: The self object
        """

        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")
        


        self.dataset_name = dataset_name
        self.nfolds = nfolds

        if models is None:
            self.models = list(models_ts_clustering_default.keys())
        else :
            self.models = models

        self.models_tsclustering = models_ts_clustering
        

    

    def model_list(self):
        """
        The model_list function prints the list of models available for use in the pipeline.
                
        :param self: Allow an object to refer to itself inside of a method
        :return: A list of the models in the model type
        """
        return print(self.models)

    def get_hyperparameters(self):
        """
        The get_hyperparameters function is used to get the hyperparameters of a model.
        
        :param self: Bind the object to the function
        :return: A dictionary of hyperparameters for each model
        """
        self.models_ = self.models_tsclustering
        self.model_params = {k:v for k,v in self.models_.items() if k in self.models}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes in a model_prefix and params.
        The model_prefix is the name of the model that will be used to prefix all hyperparameters.
        The params are a dictionary containing two keys: categorical and numerical.  The values for these keys are lists of dictionaries, each dictionary representing one hyperparameter with its associated properties (name, type, searchable).
        
        :param self: Represent the instance of the class
        :param model_prefix: Identify the model
        :param params: Pass the hyperparameters to the function
        """
        hyperparams = []
        
        for k, v in params.items():
            for p in v:
                if p.get('search')==False:
                    continue
                if k=='categorical':
                    if not p['selected']:
                        continue
                    hyperparams.append(CategoricalParamTSClustering(**{'prefix': model_prefix, 'name': p['name'], 'values': p['selected']}))
                elif k=='numerical':
                    hyperparams.append(NumericalParamTSClustering(**{'prefix': model_prefix, **p}))
        return HyperParamsTSClustering(**{'params': hyperparams})
    
    def parse_config(self):
        """
        The parse_config function is used to parse the configuration file and extract all of the information needed for
        generating a pipeline. The function takes in a config object, which contains all of the information from 
        the configuration file. It then extracts this information and stores it in class variables that can be accessed by other functions.
        
        :param self: Bind the attributes and methods of a class to an instance of that class
        """
        self.models_all = models_ts_clustering
        self.model_comp_all = models_comparison_ts_clustering
        self.model_param = self.get_hyperparameters()
        selected_models = self.models 
        self.metric = 'accuracy_score'
        self.default_imports = tsclustering_imports
        self.pipeline_params = {'dataset': self.dataset_name}
        self.shared_model_params = {'cross_validation':self.nfolds}
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def generate_code(self, output_path:str=None):
        """
        The generate_code function is used to generate the code for a given pipeline.
        
        :param self: Represent the instance of the class
        :param output_path:str: Specify the path to save the generated code
        :return: The code for all models
        """
        
        self.parse_config()
        code_list = {}
        code_append = "" #store output for each model - used for writing code file output for each model
        code_all_models = "" #store output for all models - used for copy_to_clipboard
        code, imports, requirements = TSClusteringTemplate()(self.pipeline_params)
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
        The get_code function is used to generate the code for a pipeline.
        The function takes in no arguments and returns a string of code that can be copied into an IDE or Jupyter Notebook.
        :param self: Refer to the current instance of a class
        :return: The generated code
        """
        
        code_gen = self.generate_code()
        return print(code_gen)
    
    def code_to_clipboard(self):
        """
        The code_to_clipboard function copies the generated code to the clipboard.
        
        :param self: Refer to the instance of the class
        :return: The generated code copied to clipboard
        """
        code_gen = self.generate_code()
        return pyperclip.copy(code_gen)
    
    def code_to_file(self,
                     path:str =  os.getcwd()):
        """
        The code_to_file function saves the generated code to a file.
                
                Parameters:
                    path (str): The directory where the files will be saved. Defaults to current working directory.
        
        :param self: Refer to the object itself
        :param path:str: Specify where the model files will be saved
        :return: A string that says where the model files are saved
        """
        
        self.generate_code(output_path = path)
        return f'model files saved to {path}'
    
    def model_grid_search_settings(self,model_name:str=None):
        """
        The model_grid_search_settings function is used to return the hyperparameters of a model.
        
        :param self: Bind the method to the class
        :param model_name:str: Specify the model to be used in the grid search
        :return: The hyperparameters for the model specified in the function argument
        """
        
        self.models_ = self.models_tsclf
        self.model_params = {k:v for k,v in self.models_.items() if k in model_name}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters[name]

    def set_model_grid_search_settings(self,hyperparam_dict:dict = None, model_name:list = None, path:str=None):
        """
        The set_model_grid_search_settings function is used to generate a Python script that can be run in the terminal.
        The function takes three arguments: hyperparam_dict, model_name, and path. The hyperparam_dict argument is a dictionary of 
        hyperparameters for each model that will be used in the grid search. The model name argument is a list of strings containing 
        the names of models to include in the grid search (e.g., ['RandomForestClassifier', 'XGBoost']). Finally, path is an optional string 
        argument specifying where you would like your Python script saved.
        
        :param self: Make the function a method of the class
        :param hyperparam_dict:dict: Pass in a dictionary of hyperparameters to be used for the model
        :param model_name:list: Specify which models to generate code for
        :param path:str: Save the file to a specific location
        :return: The code for the model pipeline
        :doc-author: Trelent
        """
        
        self.parse_config()
        code_append = ""
        code, imports, requirements = TSClusteringTemplate()(self.pipeline_params)
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
    