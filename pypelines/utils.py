from .sklearn.classification import models_classification
from .sklearn.regression import models_regression


def list_supported_models(model_type:str):
    if   model_type == 'classification':
        models = list(models_classification.keys())
    elif model_type == 'regression':
        models = list(models_regression.keys())
    return models