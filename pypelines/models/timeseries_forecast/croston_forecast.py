from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


croston_forecast_hyperparams = {
}



class CrostonForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'croston_forecast()'
        imports = '''from sktime.forecasting.croston  import Croston\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('Croston', model_string, croston_forecast_hyperparams, imports,model_type)


class CrostonForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'croston_forecast()'
        imports = '''from sktime.forecasting.croston  import Croston\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('Croston', model_string, croston_forecast_hyperparams, imports,model_type)
