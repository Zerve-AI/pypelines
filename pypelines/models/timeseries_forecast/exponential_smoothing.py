from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


exp_smoothing_forecast_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'sp', 'min': 12, 'max': 12, 'step': 1},
        {'search': False, 'name': 'initial_level', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'initial_trend', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'initial_seasonal', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'use_boxcox', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'smoothing_level', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'smoothing_trend', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'smoothing_seasonal', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'damping_trend', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'optimized', 'min': False, 'max': False, 'step': None},
        {'search': False, 'name': 'remove_bias', 'min': False, 'max': False, 'step': None},
        {'search': False, 'name': 'start_params', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'method', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'minimize_kwargs', 'min': None, 'max': None, 'step': None},
        {'search': False, 'name': 'use_brute', 'min': False, 'max': False, 'step': None},
        {'search': False, 'name': 'random_state', 'min': None, 'max': None, 'step': None}
    ],
    'categorical': [
        {'search': False, 'name': 'trend', 'selected': ['add'], 'values': ['add', 'mul', 'additive', 'multiplicative', None]},
        {'search': False, 'name': 'damped_trend', 'selected': [False], 'values': [True, False]},
        {'search': False, 'name': 'seasonal', 'selected': ['multiplicative'], 'values': ['add', 'mul', 'additive', 'multiplicative', None]},
        {'search': False, 'name': 'initialization_method', 'selected': ['estimated'], 'values': ['estimated', 'heuristic', 'legacy-heuristic', 'known', None]},
        {'search': False, 'name': 'use_boxcox', 'selected': [False], 'values': [True, False]}
    ]
}


class ExponentialSmoothingForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'exp_smoothing()'
        imports = '''from sktime.forecasting.exp_smoothing import ExponentialSmoothing\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ExponentialSmoothing', model_string, exp_smoothing_forecast_hyperparams, imports,model_type)


class ExponentialSmoothingForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'exp_smoothing()'
        imports = '''from sktime.forecasting.exp_smoothing  import ExponentialSmoothing\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ExponentialSmoothing', model_string, exp_smoothing_forecast_hyperparams, imports,model_type)
