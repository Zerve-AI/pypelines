from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


bats_forecast_hyperparams = {
}



class BATSForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'bats_forecast()'
        imports = '''from sktime.forecasting.bats  import BATS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('BATS', model_string, bats_forecast_hyperparams, imports,model_type)


class BATSForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'bats_forecast()'
        imports = '''from sktime.forecasting.bats  import BATS\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('BATS', model_string, bats_forecast_hyperparams, imports,model_type)


