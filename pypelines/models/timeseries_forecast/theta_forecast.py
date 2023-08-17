from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


theta_forecast_hyperparams = {
}



class ThetaForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'theta_forecast()'
        imports = '''from sktime.forecasting.theta  import ThetaForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ThetaForecaster', model_string, theta_forecast_hyperparams, imports,model_type)


class ThetaForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'theta_forecast()'
        imports = '''from sktime.forecasting.theta  import ThetaForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('ThetaForecaster', model_string, theta_forecast_hyperparams, imports,model_type)
