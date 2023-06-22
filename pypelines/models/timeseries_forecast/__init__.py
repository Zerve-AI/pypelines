from .trend_forecast import TrendForecast, TrendForecastComparison
from .naive_forecast import NaiveForecast, NaiveForecastComparison
from .polynomial_trend_forecast import PolynomialTrendForecast, PolynomialTrendForecastComparison
from .stl_forecast import STLForecast, STLForecastComparison
from .exponential_smoothing import ExponentialSmoothingForecast, ExponentialSmoothingForecastComparison
from .auto_ets import AutoETSForecast,AutoETSForecastComparison
from .theta_forecast import ThetaForecast, ThetaForecastComparison
from .croston_forecast import CrostonForecast, CrostonForecastComparison


models_forecast = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast,
    'AutoETS Forecast': AutoETSForecast,
    'Theta Forecast': ThetaForecast,
    'Croston Forecast': CrostonForecast
}

models_comparison_forecast = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison,
    'AutoETS Forecast': AutoETSForecastComparison,
    'Theta Forecast': ThetaForecastComparison,
    'Croston Forecast': CrostonForecastComparison
}



models_forecast_default = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast,
    'AutoETS Forecast': AutoETSForecast,
    'Theta Forecast': ThetaForecast,
    'Croston Forecast': CrostonForecast

}

models_comparison_forecast_default = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison,
    'AutoETS Forecast': AutoETSForecastComparison,
    'Theta Forecast': ThetaForecastComparison,
    'Croston Forecast': CrostonForecastComparison
}
