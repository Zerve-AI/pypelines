from .models.classification import models_classification
from .models.regression import models_regression
from .models.anomaly_detection import models_ad
from .models.clustering import models_clustering
from .models.timeseries_classification import models_ts_classification
from .models.timeseries_clustering import models_ts_clustering
from .models.timeseries_forecast import models_forecast
from .models.timeseries_regression import models_ts_regression
from .dataprepmethods.preprocessing import preprocessing_methods
from .dataprepmethods.outlier import outlier_methods
from .dataprepmethods.imputation import imputation_methods
from .dataprepmethods.encoding import encoding_methods
from .dataprepmethods.datetime import datetime_methods
from .dataprepmethods.discretisation import discretisation_methods
from .dataprepmethods.forecasting_features import forecasting_methods
from .dataprepmethods.transformers import transformer_methods

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
    elif model_type == 'clustering':
        models = list(models_clustering.keys())
    elif model_type == 'timeseries_clustering':
        models = list(models_ts_clustering.keys())
    elif model_type == 'timeseries_regression':
        models = list(models_ts_regression.keys())
    elif model_type == 'timeseries_classification':
        models = list(models_ts_classification.keys())
    elif model_type == 'timeseries_forecast':
        models = list(models_forecast.keys())
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
    elif method_type == 'forecasting':
        methods = list(forecasting_methods.keys())
    elif method_type == 'transformer':
        methods = list(transformer_methods.keys())
    return methods
