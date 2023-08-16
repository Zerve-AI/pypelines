from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


arima_forecast_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': False, 'name': 'method', 'selected': ["newton"], 'values': ["newton", "nm",'bfgs','lbfgs','powell','cg','ncg','basinhopping']}
    ]
}



class ARIMAForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'arima_forecast()'
        imports = '''from sktime.forecasting.arima  import ARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ARIMA', model_string, arima_forecast_hyperparams, imports,model_type)


class ARIMAForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'arima_forecast()'
        imports = '''from sktime.forecasting.arima  import ARIMA\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ARIMA', model_string, arima_forecast_hyperparams, imports,model_type)


