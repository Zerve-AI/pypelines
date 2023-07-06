from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


sf_autotheta_forecast_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'decomposition_type', 'selected': ["multiplicative"], 'values': ["multiplicative", "additive"]}
    ]
}



class SFAutoThetaForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'sf_autotheta_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoTheta\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoTheta', model_string, sf_autotheta_forecast_hyperparams, imports,model_type)


class SFAutoThetaForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'sf_autotheta_forecast()'
        imports = '''from sktime.forecasting.statsforecast  import StatsForecastAutoTheta\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('StatsForecastAutoTheta', model_string, sf_autotheta_forecast_hyperparams, imports,model_type)

