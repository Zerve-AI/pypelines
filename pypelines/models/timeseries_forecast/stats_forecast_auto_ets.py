from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


sf_autoets_forecast_hyperparams = {
}



class SFAutoETSForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'sf_autoets_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoETS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoETS', model_string, sf_autoets_forecast_hyperparams, imports,model_type)


class SFAutoETSForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'sf_autoets_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoETS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoETS', model_string, sf_autoets_forecast_hyperparams, imports,model_type)

