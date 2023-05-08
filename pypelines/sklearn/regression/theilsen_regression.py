from ..model_base import SklearnModelBase,SklearnModelComparisonBase


theilsen_regression_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'max_iter', 'min': 10, 'max': 300, 'step': 50},
        {'search': False, 'name': 'max_subpopulation', 'min': 5000, 'max': 20000, 'step': 5000},
        {'search': False, 'name': 'n_subsamples', 'min': 100, 'max': 200, 'step': 50}
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
    ]
}

class TheilSenRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'TheilSenRegressor()'
        imports = '''from sklearn.linear_model import TheilSenRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('theilsen_regression', model_string, theilsen_regression_hyperparams, imports,model_type)


class TheilSenRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ARDRegression()'
        imports = '''from sklearn.linear_model import TheilSenRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('theilsen_regression', model_string, theilsen_regression_hyperparams, imports,model_type)
