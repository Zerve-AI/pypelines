#from typing import Type
import os
import pyperclip
from .templates.pipeline import PipelineTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from .sklearn.classification import models_classification , models_comparison_classification, models_classification_default, models_comparison_classification_default
from .sklearn.regression import models_regression, models_comparison_regression, models_regression_default, models_comparison_regression_default
import pandas as pd 
from typing import Union
import inspect


classification_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
'''

regression_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
'''

class SupervisedPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 target:str,
                 model_type:str,
                 nfolds:int,
                 models:list = None):
        """
        The __init__ function initializes the class with the following parameters:
            
        
        :param self: Represent the instance of the class
        :param data:Union[str: Specify the type of data that is being passed to the function
        :param pd.DataFrame]: Check if the data is a pandas dataframe or not
        :param target:str: Specify the target variable in the dataset
        :param model_type:str: Specify the type of problem we are dealing with
        :param nfolds:int: Specify the number of folds in cross-validation
        :param models:list: Specify the list of models to be used in the experiment
        :return: A new object instance
        """
        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")

        self.dataset_name = dataset_name
        self.target = target
        self.model_type = model_type

        if models is None and model_type == 'classification':
            self.models = list(models_classification_default.keys())
        elif models is None and model_type == 'regression':
            self.models = list(models_regression_default.keys())    
        else :
            self.models = models


        self.nfolds = nfolds
        self.models_clf = models_classification
        self.models_reg = models_regression

    def model_list(self):
        """
        The models function returns a list of all the models in the car class
        
        :param self: Represent the instance of the class
        :return: A list of models
        """
        return print(self.models)

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing 
        the hyperparameter name as key and an instance of HyperParams as value. The HyperParams class is used to store information about each hyperparameter, such as its type (numerical or categorical), default value, range if numerical, etc.
        
        :param self: Bind the instance of the class to a method
        :return: A dictionary of hyperparameters for each model in the models list
        """
        if   self.model_type == 'classification':
             self.models_ = self.models_clf
        elif self.model_type == 'regression':
             self.models_ = self.models_reg
        self.model_params = {k:v for k,v in self.models_.items() if k in self.models}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes in a model prefix and the params dictionary.
        It then iterates through each key, value pair in the params dictionary. For each key, value pair it iterates through all of the values (which are dictionaries).
        If search is set to False for any of these dictionaries, it skips them. If k is equal to categorical and selected is not empty for any of these dictionaries, 
        it appends a CategoricalParam object with prefix as model_prefix and name as p['name'] (the name from that particular dictionary) 
        and values as p['selected']
        
        :param self: Represent the instance of the class
        :param model_prefix: Identify the model
        :param params: Pass the parameters to be used in the model
        :return: A hyperparams object
        """
        hyperparams = []
        
        for k, v in params.items():
            for p in v:
                if p.get('search')==False:
                    continue
                if k=='categorical':
                    if not p['selected']:
                        continue
                    hyperparams.append(CategoricalParam(**{'prefix': model_prefix, 'name': p['name'], 'values': p['selected']}))
                elif k=='numerical':
                    hyperparams.append(NumericalParam(**{'prefix': model_prefix, **p}))
        return HyperParams(**{'params': hyperparams})
    
    def parse_config(self):
        """
        The parse_config function is used to parse the configuration file and extract all of the information needed for 
        the pipeline. It extracts information about the dataset, target column, models to be trained on, hyperparameters for each model
        and other parameters such as number of folds in cross validation and metric used.
        
        :param self: Represent the instance of the class
        :return: A dictionary of models, model_params, pipeline_params and shared_model params
        """
        if self.model_type == 'classification':
           self.models_all = models_classification
           self.model_comp_all = models_comparison_classification
           self.model_param = self.get_hyperparameters()
           selected_models = self.models 
           self.metric = 'accuracy_score'
           self.default_imports = classification_imports
        elif self.model_type== 'regression':
           self.models_all = models_regression
           self.model_comp_all = models_comparison_regression
           self.model_param = self.get_hyperparameters()
           selected_models = self.models 
           self.metric = 'mean_squared_error'
           self.default_imports = regression_imports
        self.pipeline_params = {'dataset': self.dataset_name, 'target_column': self.target}
        self.shared_model_params = {'cross_validation':self.nfolds, 'metric':self.metric }
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def generate_code(self, output_path:str=None):
        """
        The generate_code function takes in a dictionary of parameters and generates code for the pipeline.
        
        :param self: Refer to the object itself
        :param output_path:str: Specify the path where the generated code will be saved
        :return: A string of code
        """
        self.parse_config()
        code_list = {}
        code_append = ""
        code, imports, requirements = PipelineTemplate()(self.pipeline_params)
        imports = self.default_imports + '\n' + imports
        code_append += imports
        code_append += code
        code_append += '\n'
        code_append += '\n'
        code_append += "##### End of Data Processing Pipeline #####"
        code_append += '\n'
        code_append += '\n'
        code_list['data_prep_pipeline'] = {'code':code_append}
        if output_path is not None:
            output_file = open(f"{output_path}/data_prep_pipeline.py", "w")
            n = output_file.write(code_append)
            output_file.close()
        for model_name, params in self.model_params.items():
            ModelTemplate= self.models_all[model_name]
            code_append = ""
            code, imports, requirements = PipelineTemplate()(self.pipeline_params)
            imports = self.default_imports + '\n' + imports
            code_append += imports
            code_append += code
            code_append += '\n'
            code_append += '\n'
            code_append += "##### End of Data Processing Pipeline #####"
            code_append += '\n'
            code_append += '\n'
            code_append += '\n'
            code_append += '\n'
            code_append += f"##### Model Pipeline for {model_name} #####"
            code_append += '\n'
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
            ModelCompTemplate= self.model_comp_all[model_name]
            code, model_imports, model_requirements  = ModelCompTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelCompTemplate().prefix, params)
                })
            code_append += f"##### Model Metrics {model_name} #####"
            code_append += code
            code_append += '\n'
            code_append += f"##### End of Model Pipeline for {model_name} #####"
            code_list[model_name] = {'code':code_append}
            if output_path is not None:
                output_file = open(f"{output_path}/{model_name}.py", "w")
                n = output_file.write(code_append)
                output_file.close()
        return code_append
    
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
        if   self.model_type == 'classification':
             self.models_ = self.models_clf
        elif self.model_type == 'regression':
             self.models_ = self.models_reg
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
        code, imports, requirements = PipelineTemplate()(self.pipeline_params)
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
    


