# from typing import Type
import os
import pyperclip
from .templates.dataprep import DataPrepTemplate
from .dataprepmethods.preprocessing import preprocessing_methods
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.imputation import imputation_methods
from .dataprepmethods.encoding import encoding_methods
from .dataprepmethods.datetime import datetime_methods
from .dataprepmethods.discretisation import discretisation_methods
from .dataprepmethods.forecasting_features import forecasting_methods
import pandas as pd 
from typing import Union
import inspect


class DataPrepPipeline:
    def __init__(self,
                 data:Union[str, pd.DataFrame],
                 target:str,
                 preprocessing_method:str=None,
                 outlier_method:str=None,
                 numerical_imputation_method:str=None,
                 categorical_imputation_method:str=None,
                 encoding_method:str=None,
                 datetime_method:str=None,
                 target_date1_column:str=None,
                 target_date2_column:str=None,
                 discretisation_method:str=None,
                 forecasting_method:str=None):

        if isinstance(data, pd.DataFrame):
            callers_globals = inspect.stack()[1][0].f_globals
            dataset_name = [k for k,v in callers_globals.items() if v is data][0]
        elif isinstance(data, str):
            dataset_name = data
        else:
            raise ValueError("data must be a pandas DataFrame or a string")
        

        self.dataset_name = dataset_name
        self.target = target
        self.preprocessing_method = preprocessing_method
        self.datetime_method = datetime_method
        self.outlier_method = outlier_method
        self.numerical_imputation = numerical_imputation_method
        self.categorical_imputation = categorical_imputation_method
        self.encoding_method = encoding_method
        self.datetime_method = datetime_method
        self.target_date1_column = target_date1_column
        self.target_date2_column = target_date2_column
        self.discretisation_method = discretisation_method
        self.forecasting_method = forecasting_method

        preprocessing_ = {k: v for k, v in preprocessing_methods.items() if k == self.preprocessing_method}
        self.preprocessing_import = {name: model().get_library() for name, model in preprocessing_.items()}

        outlier_ = {k: v for k, v in outlier_methods.items() if k == self.outlier_method}
        self.outlier_import = {name: model().get_library() for name, model in outlier_.items()}

        numerical_imputation_ = {k: v for k, v in imputation_methods.items() if k == numerical_imputation_method}
        self.numerical_imputation_import = {name: model().get_library() for name, model in numerical_imputation_.items()}

        categorical_imputation_ = {k: v for k, v in imputation_methods.items() if k == categorical_imputation_method}
        self.categorical_imputation_import = {name: model().get_library() for name, model in categorical_imputation_.items()}

        encoding_ = {k: v for k, v in encoding_methods.items() if k == self.encoding_method}
        self.encoding_import = {name: model().get_library() for name, model in encoding_.items()}

        datetime_ = {k: v for k, v in datetime_methods.items() if k == self.datetime_method}
        self.datetime_import = {name: model().get_library() for name, model in datetime_.items()}

        discretisation_ = {k: v for k, v in discretisation_methods.items() if k == self.discretisation_method}
        self.discretisation_import = {name: model().get_library() for name, model in discretisation_.items()}

        forecasting_ = {k: v for k, v in forecasting_methods.items() if k == self.forecasting_method}
        self.forecasting_import = {name: model().get_library() for name, model in forecasting_.items()}

    def parse_config(self):
        self.pipeline_params = {'dataset': self.dataset_name,
                                 'target_column': self.target,
                                 'preprocessing_method': self.preprocessing_method,
                                 'outlier_method': self.outlier_method,
                                 'numerical_imputation':self.numerical_imputation,
                                 'categorical_imputation':self.categorical_imputation,
                                 'encoding':self.encoding_method,
                                 'datetime_method':self.datetime_method,
                                 'target_date1_column': self.target_date1_column,
                                 'target_date2_column': self.target_date2_column,
                                 'discretisation_method':self.discretisation_method,
                                 'forecasting_method':self.forecasting_method
                                 }

    def generate_code(self, output_path:str=None):
        self.parse_config()

        code_append = "" #store output for each model - used for writing code file output for each model
        code_all_models = "" #store output for all models - used for copy_to_clipboard
        code, imports, requirements = DataPrepTemplate()(self.pipeline_params)
        imports = imports
        code_append += imports
        code_append += "".join(list(self.preprocessing_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.outlier_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.discretisation_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.numerical_imputation_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.categorical_imputation_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.datetime_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.encoding_import.values()))
        code_append += '\n'
        code_append += "".join(list(self.forecasting_import.values()))
        code_append += '\n'
        code_append += code
        code_append += '\n'
        code_append += "##### End of Data Processing Pipeline #####"
        code_append += '\n'
        code_append += '\n'

        code_data_prep = code_append

        code_all_models += code_data_prep
           
        return code_all_models

    def get_code(self):
        code_gen = self.generate_code()
        return print(code_gen)
    
    def code_to_clipboard(self):
        code_gen = self.generate_code()
        return pyperclip.copy(code_gen)
    
    def code_to_file(self,
                     path:str =  os.getcwd()):
        self.generate_code(output_path = path)
        return f'model files saved to {path}'