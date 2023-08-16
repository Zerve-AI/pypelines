from .models.classification import models_classification
from .models.regression import models_regression
from .models.anomaly_detection import models_ad
from .dataprepmethods.preprocessing import preprocessing_methods
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.imputation import imputation_methods
from .dataprepmethods.encoding import encoding_methods
from .dataprepmethods.datetime import datetime_methods
from .dataprepmethods.discretisation import discretisation_methods

def list_supported_models(model_type:str):
    """
    The list_supported_models function returns a list of all the supported models for a given model type.
    
    :param model_type:str: Specify the type of model to be used
    :return: A list of all the supported models
    """
    if   model_type == 'classification':
        models = list(models_classification.keys())
    elif model_type == 'regression':
        models = list(models_regression.keys())
    elif model_type == 'anomalydetection':
        models = list(models_ad.keys())
    return models


def list_supported_dataprepmethods(method_type:str):
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
