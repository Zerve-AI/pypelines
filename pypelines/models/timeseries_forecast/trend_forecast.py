from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


trend_forecast_hyperparams = {
}

class TrendForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'trend_forecaster()'
        imports = '''from sktime.forecasting.trend import TrendForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('TrendForecaster', model_string, trend_forecast_hyperparams, imports,model_type)


class TrendForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'trend_forecaster()'
        imports = '''from sktime.forecasting.trend import TrendForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('TrendForecaster', model_string, trend_forecast_hyperparams, imports,model_type)
