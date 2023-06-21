from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


naive_forecast_hyperparams = {
}

class NaiveForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'naive_forecaster()'
        imports = '''from sktime.forecasting.naive import NaiveForecaster\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('NaiveForecaster', model_string, naive_forecast_hyperparams, imports,model_type)


class NaiveForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'naive_forecaster()'
        imports = '''from sktime.forecasting.naive import TrendForecNaiveForecasteraster\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('NaiveForecaster', model_string, naive_forecast_hyperparams, imports,model_type)
