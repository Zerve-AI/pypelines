from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


sf_autoces_forecast_hyperparams = {
}



class SFAutoCESForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'sf_autoces_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoCES\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoCES', model_string, sf_autoces_forecast_hyperparams, imports,model_type)


class SFAutoCESForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'sf_autoces_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoCES\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoCES', model_string, sf_autoces_forecast_hyperparams, imports,model_type)

