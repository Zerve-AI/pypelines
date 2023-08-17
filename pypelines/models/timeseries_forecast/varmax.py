from ..model_base import TSForecastModelBase, TSForecastModelComparisonBase


varmax_forecast_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'trend', 'selected': ["c"], 'values': ["c", "ct", "ctt", "n"]},
        {'search': False, 'name': 'error_cov_type', 'selected': ["diagonal"], 'values': ["diagonal", "unstructured"]},
        {'search': False, 'name': 'cov_type', 'selected': ["opg"], 'values': ["opg", "oim","approx","robust",'robust_approx']},
        {'search': False, 'name': 'cov_kwds', 'selected': ["approx_complex_step"], 'values': ["approx_centered", "approx_complex_step"]},
        {'search': False, 'name': 'method', 'selected': ["newton"], 'values': ["newton", "nm",'bfgs','lbfgs','powell','cg','ncg','basinhopping']}
    ]
}



class VARMAXForecast(TSForecastModelBase):
    def __init__(self):
        model_string = 'varmax_forecast()'
        imports = '''from sktime.forecasting.varmax  import VARMAX\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('VARMAX', model_string, varmax_forecast_hyperparams, imports,model_type)


class VARMAXForecastComparison(TSForecastModelComparisonBase):
    def __init__(self):
        model_string = 'varmax_forecast()'
        imports = '''from sktime.forecasting.varmax  import VARMAX\nfrom sktime.forecasting.model_selection import ExpandingWindowSplitter,ForecastingGridSearchCV,ExpandingWindowSplitter\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='TSForecast'
        super().__init__('VARMAX', model_string, varmax_forecast_hyperparams, imports,model_type)


