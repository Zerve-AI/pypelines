#from typing import Type
import os
import pyperclip
from .templates.dataprep import DataPrepTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.encoding import encoding_methods
import pandas as pd 
from typing import Union
import inspect


class DataPrepPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 target:str,
                 outlier_models:list = None,
                 encoding_models:list = None):
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
        self.encoding_models = encoding_models

        #self.outlier_models = list(outlier_methods_default.keys())
        #self.encoding_models = list(encoding_methods_default.keys())    


        self.outlier_models = outlier_models
        self.encoding_models = encoding_models
        self.models_outlier = outlier_methods
        self.models_encoding = encoding_methods

    def outlier_list(self):
        """
        The models function returns a list of all the outlier methods
        
        """
        return print(outlier_methods.keys())
    

    def encoding_list(self):
        """
        The models function returns a list of all the encoding methods
        
        """
        return print(encoding_methods.keys())

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing 
        the hyperparameter name as key and an instance of HyperParams as value. The HyperParams class is used to store information about each hyperparameter, such as its type (numerical or categorical), default value, range if numerical, etc.
        
        :param self: Bind the instance of the class to a method
        :return: A dictionary of hyperparameters for each model in the models list
        """
        self.outlier_model_params = {k:v for k,v in self.models_outlier.items() if k in self.outlier_models}
        self.encoding_model_params = {k:v for k,v in self.models_encoding.items() if k in self.encoding_models}
        outlier_hyperparameters = {}
        for name, model in self.outlier_model_params.items():
            outlier_hyperparameters[name] = model().get_hyperparameters()

        encoding_hyperparameters = {}
        for name, model in self.encoding_model_params.items():
            encoding_hyperparameters[name] = model().get_hyperparameters()
        return outlier_hyperparameters, encoding_hyperparameters
    
    def parse_config(self):
        """
        The parse_config function is used to parse the configuration file and extract all of the information needed for 
        the pipeline. It extracts information about the dataset, target column, models to be trained on, hyperparameters for each model
        and other parameters such as number of folds in cross validation and metric used.
        
        :param self: Represent the instance of the class
        :return: A dictionary of models, model_params, pipeline_params and shared_model params
        """

        self.outlier_models_all = outlier_methods
        self.encoding_models_all = encoding_methods
        self.outlier_model_param, self.encoding_model_param = self.get_hyperparameters()
        outlier_selected_models = self.outlier_models 
        encoding_selected_models = self.encoding_models 


        self.pipeline_params = {'dataset': self.dataset_name, 'target': self.target, 'encoding_models': self.encoding_models}
        #self.shared_model_params = {'cross_validation':self.nfolds, 'metric':self.metric }
        self.outlier_model_params = {k:v for k,v in self.outlier_model_param.items() if k in outlier_selected_models}
        self.encoding_model_params = {k:v for k,v in self.encoding_model_param.items() if k in encoding_selected_models}

    def generate_code(self, output_path:str=None):
        """
        The generate_code function takes in a dictionary of parameters and generates code for the pipeline.
        
        :param self: Refer to the object itself
        :param output_path:str: Specify the path where the generated code will be saved
        :return: A string of code
        """
        self.parse_config()
        code_list = {}
        code_append = "" #store output for each model - used for writing code file output for each model
        code_all_models = "" #store output for all models - used for copy_to_clipboard
        code, imports, requirements = DataPrepTemplate()(self.pipeline_params)
        imports = imports
        code_append += imports
        for model_name, params in self.encoding_model_params.items():
            code_append += params
            code_append += '\n'
        for model_name, params in self.outlier_model_params.items():
            code_append += params

        code_append += '\n'
        code_append += '\n'
        code_append += code
        code_append += '\n'
        code_append += '\n'
        code_append += "##### End of Data Processing Pipeline #####"
        code_append += '\n'
        code_append += '\n'
        code_append += '\n'
        code_append += '\n'

        code_data_prep = code_append

        code_all_models += code_data_prep
           
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

