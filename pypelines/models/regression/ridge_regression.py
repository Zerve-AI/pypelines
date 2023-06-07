from ..model_base import SklearnModelBase,SklearnModelComparisonBase


ridge_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 2, 'step': .5},
        {'search': False, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'search': False, 'name': 'positive', 'selected': [True], 'values': [True, False]}
    ]
}

class RidgeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import Ridge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('ridge_regression', model_string, ridge_regression_hyperparams, imports,model_type)


class RidgeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import Ridge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('ridge_regression', model_string, ridge_regression_hyperparams, imports,model_type)
