from .dataprepmethods.preprocessing import preprocessing_methods
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.imputation import imputation_methods
from .dataprepmethods.encoding import encoding_methods
from .dataprepmethods.datetime import datetime_methods
from .dataprepmethods.discretisation import discretisation_methods


def list_supported_methods(method_type:str):
    if   method_type == 'outlier':
        methods = list(outlier_methods.keys())
    elif method_type == 'imputation':
        methods = list(imputation_methods.keys())
    elif method_type == 'encoding':
        methods = list(encoding_methods.keys())
    elif method_type == 'datetime':
        methods = list(datetime_methods.keys())
    elif method_type == 'preprocessing':
        methods = list(preprocessing_methods.keys())
    elif method_type == 'discretisation':
        methods = list(discretisation_methods.keys())
    return methods

