#from typing import Type
import os
import pyperclip
from .templates.ts_forecast_dataprep import TSTemplate
from .schemas import HyperParamsTSF, NumericalParamTSF, CategoricalParamTSF
from .models.timeseries_forecast import models_comparison_forecast, models_forecast, models_comparison_forecast_default, models_forecast_default
import pandas as pd 
from typing import Union
import inspect


tsf_imports = '''
from sktime import *
from sklearn.metrics import mean_squared_error
'''

class TSForecastPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 models:list = None,
                 target_column:str=None,
                 date_column:str = None,
                 date_format:str = None,
                 frequency:str = None,
                 forecast_horizon:list = None,
                 use_exogeneous_vars:str = 'False'):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance variables for each object that will be created.
        
        :param self: Represent the instance of the class
        :param data:Union[str: Specify that the data parameter can be either a string or a pandas dataframe
        :param pd.DataFrame]: Pass the dataframe to the class
        :param models:list: Specify the models to be used in forecasting
        :param target_column:str: Specify the name of the column to be forecasted
        :param date_column:str: Specify the name of the column in your dataframe that contains dates
        :param date_format:str: Specify the format of the date column
        :param frequency:str: Define the frequency of the time series
        :param forecast_horizon:list: Define the number of periods to forecast
        :param use_exogeneous_vars:str: Determine whether or not to use exogenous variables in the model
        :return: A new instance of the class
        """
        
        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")


        self.dataset_name = dataset_name
        self.date_column = date_column
        self.frequency = frequency
        self.date_format = date_format
        self.forecast_horizon = forecast_horizon
        self.target_column = target_column
        self.exo = use_exogeneous_vars

        if models is None:
            self.models = list(models_forecast_default.keys())
        else :
            self.models = models

        self.models_tsf = models_forecast

    

    def model_list(self):
        """
        The model_list function returns a list of all the models that are available to be used in the pipeline.
        
        
        :param self: Represent the instance of the class
        :return: The list of models in the car
        :doc-author: Trelent
        """
        return print(self.models)

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing all 
        the hyperparameters for that model. The format is as follows:
        
        :param self: Bind the object to the method
        :return: A dictionary of hyperparameters for each model
        """
        
        self.models_ = self.models_tsf
        self.model_params = {k:v for k,v in self.models_.items() if k in self.models}
        hyperparameters = {}
        for name, model in self.model_params.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes in a model_prefix and params dictionary.
        The function then iterates through the params dictionary, which is structured as follows:
        {'categorical': [{'name': '', 'selected': []}, ...], 
         'numerical': [{'name': '', 'min_value: 0, max_value: 1, search=True/False}]}
        and returns a HyperParamsTSF object with all of the hyperparameters that are to be searched over.
        
        :param self: Bind the method to an object
        :param model_prefix: Identify the model
        :param params: Pass the hyperparameters to be used in the search
        :return: A hyperparamstsf object
        """
        
        hyperparams = []
        
        for k, v in params.items():
            for p in v:
                if p.get('search')==False:
                    continue
                if k=='categorical':
                    if not p['selected']:
                        continue
                    hyperparams.append(CategoricalParamTSF(**{'prefix': model_prefix, 'name': p['name'], 'values': p['selected']}))
                elif k=='numerical':
                    hyperparams.append(NumericalParamTSF(**{'prefix': model_prefix, **p}))
        return HyperParamsTSF(**{'params': hyperparams})
    
    def parse_config(self):
        """
        The parse_config function is used to parse the configuration file and extract all of the information needed for
        the pipeline. It also sets up some default values that are used in other parts of the pipeline.
        :param self: Refer to the class instance itself
        """
        
        self.models_all = models_forecast
        self.model_comp_all = models_comparison_forecast
        self.model_param = self.get_hyperparameters()
        selected_models = self.models 
        self.metric = 'mean_squared_error'
        self.default_imports = tsf_imports
        self.pipeline_params = {'dataset': self.dataset_name,
                                'date_column':self.date_column,
                                'date_format':self.date_format,
                                'target_column':self.target_column,
                                'frequency':self.frequency,
                                'exo':self.exo}
        self.shared_model_params = {'metric':self.metric ,'forecast_horizon':self.forecast_horizon,'exo':self.exo}
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def generate_code(self, output_path:str=None):
        """
        The generate_code function is used to generate the code for a time series forecasting pipeline.
        
        :param self: Refer to the class instance itself
        :param output_path:str: Specify the path where the generated code is saved
        :return: A string that contains the code for all models in the pipeline
        """
        
        self.parse_config()
        code_list = {}
        code_append = "" #store output for each model - used for writing code file output for each model
        code_all_models = "" #store output for all models - used for copy_to_clipboard
        code, imports, requirements = TSTemplate()(self.pipeline_params)
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
                It takes in no arguments and returns a string of code that can be executed.
                
        
        :param self: Refer to the current class instance
        :return: The code generated by the generate_code function
        """
        
        code_gen = self.generate_code()
        return print(code_gen)
    
    def code_to_clipboard(self):
        """
        The code_to_clipboard function copies the generated code to the clipboard.
                
        
        :param self: Refer to the object itself
        :return: A string of the code generated
        """
        
        code_gen = self.generate_code()
        return pyperclip.copy(code_gen)
    
    def code_to_file(self,
                     path:str =  os.getcwd()):
        """
        The code_to_file function saves the generated code to a file.
                
                Parameters:
                    path (str): The directory where the files will be saved. Defaults to current working directory.
        
        :param self: Represent the instance of the class
        :param path:str: Specify the path where the model files will be saved
        :return: path to which the files are saved.
        """
        
        self.generate_code(output_path = path)
        return f'model files saved to {path}'
    