from ..model_base import SklearnModelBase,SklearnModelComparisonBase


poisson_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 2, 'step': 0.5},
        {'search': False, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
    ]
}

class PoissonRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'PoissonRegressor()'
        imports = '''from sklearn.linear_model import PoissonRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('poisson_regression', model_string, poisson_regression_hyperparams, imports,model_type)


class PoissonRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'PoissonRegressor()'
        imports = '''from sklearn.linear_model import PoissonRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('poisson_regression', model_string, poisson_regression_hyperparams, imports,model_type)
