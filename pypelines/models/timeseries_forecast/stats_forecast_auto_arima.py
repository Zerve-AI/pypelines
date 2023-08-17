from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


sf_autoarima_forecast_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'information_criterion', 'selected': ["aicc"], 'values': ["aicc", "aic", "bic"]}
    ]
}



class SFAutoArimaForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'sf_autoarima_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoARIMA', model_string, sf_autoarima_forecast_hyperparams, imports,model_type)


class SFAutoArimaForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'sf_autoarima_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoARIMA', model_string, sf_autoarima_forecast_hyperparams, imports,model_type)

