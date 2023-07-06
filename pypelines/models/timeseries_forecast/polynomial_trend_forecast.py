from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


polynomial_trend_forecast_hyperparams = {
}

class PolynomialTrendForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'polynomial_trend_forecaster()'
        imports = '''from sktime.forecasting.trend import PolynomialTrendForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('PolynomialTrendForecaster', model_string, polynomial_trend_forecast_hyperparams, imports,model_type)


class PolynomialTrendForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'polynomial_trend_forecaster()'
        imports = '''from sktime.forecasting.trend import PolynomialTrendForecaster\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('PolynomialTrendForecaster', model_string, polynomial_trend_forecast_hyperparams, imports,model_type)
