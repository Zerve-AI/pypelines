from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


var_forecast_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'trend', 'selected': ["c"], 'values': ["c", "ct", "ctt", "n"]},
        {'search': True, 'name': 'ic', 'selected': ["aic"], 'values': ["aic", "fpe", "hqic", "bic"]}
    ]
}



class VARForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'var_forecast()'
        imports = '''from sktime.forecasting.var  import VAR\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('VAR', model_string, var_forecast_hyperparams, imports,model_type)


class VARForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'var_forecast()'
        imports = '''from sktime.forecasting.var  import VAR\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('VAR', model_string, var_forecast_hyperparams, imports,model_type)


