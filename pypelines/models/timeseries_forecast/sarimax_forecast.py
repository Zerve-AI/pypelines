from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


sarimax_forecast_hyperparams = {
}



class SarimaxForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'sarimax_forecast()'
        imports = '''from sktime.forecasting.sarimax  import SARIMAX\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('SARIMAX', model_string, sarimax_forecast_hyperparams, imports,model_type)


class SarimaxForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'sarimax_forecast()'
        imports = '''from sktime.forecasting.sarimax  import SARIMAX\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('SARIMAX', model_string, sarimax_forecast_hyperparams, imports,model_type)


