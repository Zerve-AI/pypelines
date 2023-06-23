from .trend_forecast import TrendForecast, TrendForecastComparison
from .naive_forecast import NaiveForecast, NaiveForecastComparison
from .polynomial_trend_forecast import PolynomialTrendForecast, PolynomialTrendForecastComparison
from .stl_forecast import STLForecast, STLForecastComparison
from .exponential_smoothing import ExponentialSmoothingForecast, ExponentialSmoothingForecastComparison
from .auto_ets import AutoETSForecast,AutoETSForecastComparison
from .theta_forecast import ThetaForecast, ThetaForecastComparison
from .croston_forecast import CrostonForecast, CrostonForecastComparison
from .stats_forecast_auto_arima import SFAutoArimaForecast, SFAutoArimaForecastComparison
from .stats_forecast_auto_ces import SFAutoCESForecast, SFAutoCESForecastComparison
from .stats_forecast_auto_ets import SFAutoETSForecast, SFAutoETSForecastComparison
from .stats_forecast_auto_theta import SFAutoThetaForecast, SFAutoThetaForecastComparison
from .sarimax_forecast import SarimaxForecast, SarimaxForecastComparison
from .var import VARForecast, VARForecastComparison
from .varmax import VARMAXForecast, VARMAXForecastComparison
from .autoarima import AutoARIMAForecast, AutoARIMAForecastComparison
from .arima import ARIMAForecast, ARIMAForecastComparison
from .bats import BATSForecast, BATSForecastComparison
from .tbats import TBATSForecast, TBATSForecastComparison


models_forecast = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast,
    'AutoETS Forecast': AutoETSForecast,
    'Theta Forecast': ThetaForecast,
    'Croston Forecast': CrostonForecast,
    'SFAutoArima Forecast': SFAutoArimaForecast,
    'SFAutoCES Forecast': SFAutoCESForecast,
    'SFAutoETS Forecast': SFAutoETSForecast,
    'SFAutoTheta Forecast': SFAutoThetaForecast,
    'SARIMAX': SarimaxForecast,
    'VAR' : VARForecast,
    'VARMAX' : VARMAXForecast,
    'AutoARIMA': AutoARIMAForecast,
    'ARIMA': ARIMAForecast,
    'BATS': BATSForecast,
    'TBATS': TBATSForecast
}

models_comparison_forecast = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison,
    'AutoETS Forecast': AutoETSForecastComparison,
    'Theta Forecast': ThetaForecastComparison,
    'Croston Forecast': CrostonForecastComparison,
    'SFAutoArima Forecast': SFAutoArimaForecastComparison,
    'SFAutoCES Forecast': SFAutoCESForecastComparison,
    'SFAutoETS Forecast': SFAutoETSForecastComparison,
    'SFAutoTheta Forecast': SFAutoThetaForecastComparison,
    'SARIMAX': SarimaxForecastComparison,
    'VAR' : VARForecastComparison,
    'VARMAX' : VARMAXForecastComparison,
    'AutoARIMA': AutoARIMAForecastComparison,
    'ARIMA': ARIMAForecastComparison,
    'BATS': BATSForecastComparison,
    'TBATS': TBATSForecastComparison
}



models_forecast_default = {
    'Trend Forecast': TrendForecast,
    'Naive Forecast': NaiveForecast,
    'Polynomial Trend Forecast': PolynomialTrendForecast,
    'STL Forecast': STLForecast,
    'Exponential Smoothing': ExponentialSmoothingForecast,
    'AutoETS Forecast': AutoETSForecast,
    'Theta Forecast': ThetaForecast,
    'Croston Forecast': CrostonForecast,
    'SFAutoArima Forecast': SFAutoArimaForecast,
    'SFAutoCES Forecast': SFAutoCESForecast,
    'SFAutoETS Forecast': SFAutoETSForecast,
    'SFAutoTheta Forecast': SFAutoThetaForecast,
    'SARIMAX': SarimaxForecast,
    'VAR' : VARForecast,
    'VARMAX' : VARMAXForecast,
    'AutoARIMA': AutoARIMAForecast,
    'ARIMA': ARIMAForecast,
    'BATS': BATSForecast,
    'TBATS': TBATSForecast
}

models_comparison_forecast_default = {
    'Trend Forecast': TrendForecastComparison,
    'Naive Forecast': NaiveForecastComparison,
    'Polynomial Trend Forecast': PolynomialTrendForecastComparison,
    'STL Forecast': STLForecastComparison,
    'Exponential Smoothing': ExponentialSmoothingForecastComparison,
    'AutoETS Forecast': AutoETSForecastComparison,
    'Theta Forecast': ThetaForecastComparison,
    'Croston Forecast': CrostonForecastComparison,
    'SFAutoArima Forecast': SFAutoArimaForecastComparison,
    'SFAutoCES Forecast': SFAutoCESForecastComparison,
    'SFAutoETS Forecast': SFAutoETSForecastComparison,
    'SFAutoTheta Forecast': SFAutoThetaForecastComparison,
    'SARIMAX': SarimaxForecastComparison,
    'VAR' : VARForecastComparison,
    'VARMAX' : VARMAXForecastComparison,
    'AutoARIMA': AutoARIMAForecastComparison,
    'ARIMA': ARIMAForecastComparison,
    'BATS': BATSForecastComparison,
    'TBATS': TBATSForecastComparison
}
