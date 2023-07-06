from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


auto_ets_forecast_hyperparams = {'numerical': [
    {'search': True, 'name': 'sp','min': 12, 'max': 13, 'step': 1},
    {'search': False, 'name': 'initial_level','min': 12, 'max': 13, 'step': 1},
    {'search': False, 'name': 'initial_trend','min': 12, 'max': 13, 'step': 1},
    {'search': False, 'name': 'initial_seasonal','min': 12, 'max': 13, 'step': 1},
    {'search': False, 'name': 'maxiter','min': 12, 'max': 13, 'step': 1}
],

'categorical': [
    {'search': True, 'name': 'error', 'selected': ['add'], 'values': ['add', 'mul']},
    {'search': True, 'name': 'trend', 'selected': [None], 'values': ['add', 'mul', None]},
    {'search': True, 'name': 'seasonal', 'selected': [None], 'values': ['add', 'mul', None]},
    {'search': True, 'name': 'initialization_method', 'selected': ['estimated'], 'values': ['estimated', 'heuristic', 'known']},
    {'search': True, 'name': 'bounds', 'selected': [None], 'values': [None]},
    {'search': True, 'name': 'auto', 'selected': [False], 'values': [True, False]},
    {'search': True, 'name': 'information_criterion', 'selected': ['aic'], 'values': ['aic', 'bic', 'aicc']},
    {'search': True, 'name': 'allow_multiplicative_trend', 'selected': [False], 'values': [True, False]},
    {'search': True, 'name': 'restrict', 'selected': [True], 'values': [True, False]},
    {'search': True, 'name': 'additive_only', 'selected': [False], 'values': [True, False]},
    {'search': True, 'name': 'ignore_inf_ic', 'selected': [True], 'values': [True, False]},
]
}



class AutoETSForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'autoets_forecast()'
        imports = '''from sktime.forecasting.ets  import AutoETS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('AutoETS', model_string, auto_ets_forecast_hyperparams, imports,model_type)


class AutoETSForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'autoets_forecast()'
        imports = '''from sktime.forecasting.ets  import AutoETS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('AutoETS', model_string, auto_ets_forecast_hyperparams, imports,model_type)
