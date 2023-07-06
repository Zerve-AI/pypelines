from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


stl_forecast_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'sp', 'min': 2, 'max': 2, 'step': 1},
        {'search': False, 'name': 'seasonal', 'min': 3, 'max': 2, 'step': 2},
        {'search': False, 'name': 'trend', 'min': 2, 'max': 2, 'step': 2},
        {'search': False, 'name': 'low_pass', 'min': 3, 'max': 3, 'step': 2},
        {'search': False, 'name': 'seasonal_deg', 'min': 0, 'max': 1, 'step': 1},
        {'search': False, 'name': 'trend_deg', 'min': 0, 'max': 1, 'step': 1},
        {'search': False, 'name': 'low_pass_deg', 'min': 0, 'max': 1, 'step': 1},
        {'search': False, 'name': 'seasonal_jump', 'min': 1, 'max': 1, 'step': 1},
        {'search': False, 'name': 'trend_jump', 'min': 1, 'max': 1, 'step': 1},
        {'search': False, 'name': 'low_pass_jump', 'min': 1, 'max': 1, 'step': 1},
        {'search': False, 'name': 'inner_iter', 'min': 1, 'max': 1, 'step': 1},
        {'search': False, 'name': 'outer_iter', 'min': 1, 'max': 1, 'step': 1}
    ],
    'categorical': [
        {'search': False, 'name': 'forecaster_trend', 'selected': ['None'], 'values': [None]},
        {'search': False, 'name': 'forecaster_seasonal', 'selected': ['None'], 'values': [None]},
        {'search': False, 'name': 'forecaster_resid', 'selected': ['None'], 'values': [None]},
    ]
}

class STLForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'stl_forecaster()'
        imports = '''from sktime.forecasting.trend import STLForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('STLForecaster', model_string, stl_forecast_hyperparams, imports,model_type)


class STLForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'stl_forecaster()'
        imports = '''from sktime.forecasting.trend import STLForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('STLForecaster', model_string, stl_forecast_hyperparams, imports,model_type)
