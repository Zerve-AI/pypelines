#from typing import Type
import os
import pyperclip
from .templates.dataprep import DataPrepTemplate
from .templates.discretisation import DataPrepModelTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.encoding import encoding_methods
from .dataprepmethods.discretisation import discretisation_methods
import pandas as pd 
from typing import Union
import inspect


class DataPrepPipeline:
    def __init__(self, data: Union[str, pd.DataFrame], target: str,
                 outlier_models: list = None, encoding_models: list = None,
                 discretisation_models: list = None):
        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k, v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")

        self.dataset_name = dataset_name
        self.target = target
        self.encoding_models = encoding_models or []
        self.discretisation_models = discretisation_models or []
        self.outlier_models = outlier_models or []

 
        self.outlier_models = outlier_models
        self.encoding_models = encoding_models
        self.models_outlier = outlier_methods
        self.models_encoding = encoding_methods
        self.models_discretisation = discretisation_methods

        # Add initialization of other model-related attributes

    def outlier_list(self):
        return list(outlier_methods.keys())

    def encoding_list(self):
        return list(encoding_methods.keys())

    def discretisation_list(self):
        return list(discretisation_methods.keys())

    def get_code(self):
        code_gen = self.generate_code()
        return code_gen

    def code_to_clipboard(self):
        code_gen = self.generate_code()
        return pyperclip.copy(code_gen)

    def code_to_file(self, path: str = os.getcwd()):
        self.generate_code(output_path=path)
        return f"Model files saved to {path}"
    
    def get_hyperparameters(self):
        try:
            self.outlier_model_params = {k: v for k, v in self.models_outlier.items() if k in self.outlier_models}
            self.encoding_model_params = {k: v for k, v in self.models_encoding.items() if k in self.encoding_models}

            outlier_hyperparameters = {name: model().get_hyperparameters() for name, model in self.outlier_model_params.items()}
            encoding_hyperparameters = {name: model().get_hyperparameters() for name, model in self.encoding_model_params.items()}

            discretisation_hyperparameters = {}
            self.discretisation_model_params = {k: v for k, v in self.models_discretisation.items() if k in self.discretisation_models}
            discretisation_hyperparameters = {name: model().get_hyperparameters() for name, model in self.discretisation_model_params.items()}

            return outlier_hyperparameters, encoding_hyperparameters, discretisation_hyperparameters
        except Exception as e:
            raise RuntimeError(f"An error occurred while getting hyperparameters: {e}")


    def generate_code(self, output_path: str = None):
        try:
            self.parse_config()        
            code_append = "" #store output for each model - used for writing code file output for each model

            # Data Preparation
            code, imports, requirements = DataPrepTemplate()(self.pipeline_params)
            code_append += imports
            # Loading the library for encoding and outlier handling
            for model_name, params in self.encoding_model_params.items():
                code_append += params
                code_append += '\n'
            for model_name, params in self.outlier_model_params.items():
                code_append += params
            code_append += code
            code_append += '\n'
            # Loading discretisation as optional
            if self.discretisation_models:
                code_append += "# DISCRETISATION"
                code_append += '\n'
                discretisation_code = ""
                # Loading library for discretisation
                for model_name, params in self.discretisation_model_params.items():
                    discretisation_code += params
                # Loading code for discretisation
                if self.pipeline_params['discretisation_models']:
                    discretisation_code += DataPrepModelTemplate()(self.pipeline_params)[0]
                    
                code_append += discretisation_code
            
            code_append += "##### End of Data Processing Pipeline #####"

            final_code = code_append
            if output_path:
                with open(output_path, "w") as code_file:
                    code_file.write(final_code)

            return final_code
        except Exception as e:
            return f"An error occurred: {e}"

    def parse_config(self):
        try:
            self.outlier_models_all = outlier_methods
            self.encoding_models_all = encoding_methods
            
            outlier_selected_models = self.outlier_models 
            encoding_selected_models = self.encoding_models 

            discretisation_selected_models = self.discretisation_models
            self.outlier_model_param, self.encoding_model_param, self.discretisation_model_param = self.get_hyperparameters()
            self.pipeline_params = {'dataset': self.dataset_name, 'target': self.target, 'encoding_models': self.encoding_models, 'discretisation_models' : self.discretisation_models}
            self.outlier_model_params = {k:v for k,v in self.outlier_model_param.items() if k in outlier_selected_models}
            self.encoding_model_params = {k:v for k,v in self.encoding_model_param.items() if k in encoding_selected_models}
            self.discretisation_model_params = {k:v for k,v in self.discretisation_model_param.items() if k in discretisation_selected_models}

        except Exception as e:
            raise RuntimeError(f"Error parsing configuration: {e}")



