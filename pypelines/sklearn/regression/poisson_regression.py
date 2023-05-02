from ..model_base import SklearnModelBase,SklearnModelComparisonBase


poisson_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.005},
        {'checked': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'solver', 'selected': ["lbfgs"], 'values': ["lbfgs", "newton-cholesky"]},
        {'checked': True, 'name': 'warm_start', 'selected': [True], 'values': [True, False]}
    ]
}

class PoissonRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import PoissonRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('poisson_regression', model_string, poisson_regression_hyperparams, imports,model_type)


class PoissonRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import PoissonRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('poisson_regression', model_string, poisson_regression_hyperparams, imports,model_type)
