from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


naive_forecast_hyperparams = {
        'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'strategy', 'selected': ["last"], 'values': ["last", "mean", "drift"]}
    ]
}

class NaiveForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'naive_forecaster()'
        imports = '''from sktime.forecasting.naive import NaiveForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('NaiveForecaster', model_string, naive_forecast_hyperparams, imports,model_type)


class NaiveForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'naive_forecaster()'
        imports = '''from sktime.forecasting.naive import NaiveForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('NaiveForecaster', model_string, naive_forecast_hyperparams, imports,model_type)
