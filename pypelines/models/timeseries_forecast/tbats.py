from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


tbats_forecast_hyperparams = {
}



class TBATSForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'tbats_forecast()'
        imports = '''from sktime.forecasting.tbats  import TBATS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('TBATS', model_string, tbats_forecast_hyperparams, imports,model_type)


class TBATSForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'tbats_forecast()'
        imports = '''from sktime.forecasting.tbats  import TBATS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('TBATS', model_string, tbats_forecast_hyperparams, imports,model_type)


