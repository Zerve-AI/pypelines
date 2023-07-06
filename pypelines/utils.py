from .models.classification import models_classification
from .models.regression import models_regression
from .models.anomaly_detection import models_ad
from .models.timeseries_forecast import models_forecast


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
    elif model_type == 'timeseries_forecast':
        models = list(models_forecast.keys())
    return models



