from typing import Type
import pandas as pd
import os
from .templates.pipeline import PipelineTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from .sklearn.classification import models_classification , model_comparison_classification
from .sklearn.regression import models_regression, model_comparison_regression

classification_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
'''

regression_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
'''

class SklearnPipeline:
    def __init__(self,
                 data:str,
                 target:str,
                 model_type:str,
                 models:list,
                 nfolds:int,
                 output_folder:str =  os.getcwd(),
                 output_format:str = 'code'):
        """
        The __init__ function is the constructor for a class.
        It initializes all of the attributes of an object, and it's called when you create a new instance of that class.
        
        
        :param self: Represent the instance of the class
        :param data:str: Specify the path to the data file
        :param target:str: Specify the target variable in the dataset
        :param model_type:str: Specify the type of model you want to use
        :param models:list: Pass a list of models to the class
        :param nfolds:int: Specify the number of folds for cross-validation
        :param output_folder:str: Specify the folder where the output files will be saved. If it's not specified then files get saved to home directory
        :param output_format:str: Define the output format - 'code' - shows output on the console, 'script' - save to output directory
        """
        
        self.data = data
        self.target = target
        self.model_type = model_type
        self.models = models
        self.nfolds = nfolds
        self.models_clf = models_classification
        self.models_reg = models_regression
        self.output_type = output_format
        self.output_folder = output_folder

    def model_list(self):
        """
        The models function returns a list of all the models in the car class
        
        :param self: Represent the instance of the class
        :return: A list of models
        """
        return print(self.models)
    

    def get_settings_classification(self):
        """
        The get_settings_classification function returns a dictionary of hyperparameters for each model.
            The keys are the names of the models and the values are dictionaries containing all possible 
            hyperparameter settings for that model.
        
        :param self: Represent the instance of the class
        :return: A dictionary of hyperparameters for each model
        """
        hyperparameters = {}
        for name, model in self.models_clf.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def get_settings_regression(self):
        """
        The get_settings_regression function returns a dictionary of hyperparameters for each model.
            The keys are the names of the models and the values are dictionaries containing all 
            hyperparameters for that model.
        
        :param self: Represent the instance of the class
        :return: A dictionary of hyperparameters for each model
        """
        hyperparameters = {}
        for name, model in self.models_reg.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes a model_prefix and params dictionary as input.
        The model_prefix is the name of the model, e.g., 'xgb'. The params dictionary contains two keys:
        'categorical' and 'numerical'. Each key has a list of dictionaries as its value. 
        Each dictionary in this list represents one hyperparameter for that type (categorical or numerical). 
        For example, if we have three categorical hyperparameters with names &quot;a&quot;, &quot;b&quot;, and &quot;c&quot; then the value for 
        the key 'categorical' will be [{
        
        :param self: Represent the instance of the class
        :param model_prefix: Identify the model
        :param params: Pass in the hyperparameters that you want to use
        :return: A hyperparams object
        """
        hyperparams = []
        for k, v in params.items():
            for p in v:
                if p.get('checked')==False:
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
        The parse_config function is used to parse the user input parameters and set up the model parameters.
        =The function then sets up all of the necessary variables for running 
        the models, including:
        
        :param self: Refer to the instance of the class
        :return: A dictionary of models and their parameters
        """
        if self.model_type == 'classification':
           self.models_all = models_classification
           self.model_comp_all = model_comparison_classification
           self.model_param = self.get_settings_classification()
           selected_models = self.models 
           self.metric = 'accuracy_score'
           self.default_imports = classification_imports
        elif self.model_type== 'regression':
           self.models_all = models_regression
           self.model_comp_all = model_comparison_regression
           self.model_param = self.get_settings_regression()
           selected_models = self.models 
           self.metric = 'mean_squared_error'
           self.default_imports = regression_imports
        self.pipeline_params = {'dataset': self.data, 'target_column': self.target}
        self.shared_model_params = {'cross_validation':self.nfolds, 'metric':self.metric }
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def generate_code(self):
        """
        The generate_code function takes the parameters from the config file and generates a python script that can be run to train, evaluate, and save models.
        
        :param self: Access the attributes and methods of the class
        :return: A string of code
        """
        self.parse_config()

        if self.output_type == 'code':
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
            return code_append

        elif self.output_type =='script':
            code_list = {}
            code_pipeline = ""
            code, imports, requirements = PipelineTemplate()(self.pipeline_params)
            imports = self.default_imports + '\n' + imports
            code_pipeline += imports
            code_pipeline += code
            code_pipeline += '\n'
            code_pipeline += '\n'
            code_pipeline += "##### End of Data Processing Pipeline #####"
            code_pipeline += '\n'
            code_pipeline += '\n'
            code_list['data_prep_pipeline'] = {'code':code_pipeline}
            output_file = open(f"{self.output_folder}/data_prep_pipeline.py", "w")
            n = output_file.write(code_pipeline)
            output_file.close()
            for model_name, params in self.model_params.items():
                code_append = ""
                ModelTemplate= self.models_all[model_name]
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
                output_file = open(f"{self.output_folder}/{model_name}.py", "w")
                n = output_file.write(code_append)
                output_file.close()

            return code_list
    
    def grid_search(self):
        """
        The grid_search function is used to parse the config file and return a dictionary of model parameters.
                The function will be called by the main script, which will then pass these parameters into the 
                train_model function. This allows for easy modification of model hyperparameters without having to 
                change code in multiple places.
        
        :param self: Represent the instance of the class
        :return: A dictionary of the parameters to be used in the model
        """
        self.parse_config()
        return self.model_params
    
    def get_code(self):
        """
        The get_code function is a method of the class CodeGenerator.
        It takes no arguments and returns the generated code as a string.
        
        :param self: Represent the instance of the class
        :return: The value of the generate_code function
        """
        code_gen = self.generate_code()
        return print(code_gen)

