from .sklearn.classification import models_classification
from .sklearn.regression import models_regression


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
    return models



