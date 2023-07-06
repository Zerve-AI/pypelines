from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


autoarima_forecast_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'maxiter', 'min': 10, 'max': 100, 'step': 10},
        {'search': True, 'name': 'start_p', 'min': 1, 'max': 5, 'step': 1},
        {'search': True, 'name': 'start_q', 'min': 1, 'max': 5, 'step': 1},
        {'search': True, 'name': 'start_P', 'min': 1, 'max': 5, 'step': 1},
        {'search': True, 'name': 'start_Q', 'min': 1, 'max': 5, 'step': 1},
    ],
    'categorical': [
        {'search': False, 'name': 'method', 'selected': ["newton"], 'values': ["newton", "nm",'bfgs','lbfgs','powell','cg','ncg','basinhopping']}
    ]
}



class AutoARIMAForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'autoarima_forecast()'
        imports = '''from sktime.forecasting.arima  import AutoARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('AutoARIMA', model_string, autoarima_forecast_hyperparams, imports,model_type)


class AutoARIMAForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'autoarima_forecast()'
        imports = '''from sktime.forecasting.arima  import AutoARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('AutoARIMA', model_string, autoarima_forecast_hyperparams, imports,model_type)


