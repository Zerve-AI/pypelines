from .trend_forecast import TrendForecast, TrendForecastComparison
from .naive_forecast import NaiveForecast, NaiveForecastComparison
from .polynomial_trend_forecast import PolynomialTrendForecast, PolynomialTrendForecastComparison
from .stl_forecast import STLForecast, STLForecastComparison
from .exponential_smoothing import ExponentialSmoothingForecast, ExponentialSmoothingForecastComparison

models_forecast = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast
}

models_comparison_forecast = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison
}



models_forecast_default = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast
}

models_comparison_forecast_default = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison
}
