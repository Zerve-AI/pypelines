from ..model_base import SklearnModelBase,SklearnModelComparisonBase


ridge_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 10, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'positive', 'selected': [True], 'values': [True, False]}
    ]
}

class RidgeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import Ridge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('ridge_regression', model_string, ridge_regression_hyperparams, imports,model_type)


class RidgeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Ridge()'
        imports = '''from sklearn.linear_model import Ridge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('ridge_regression', model_string, ridge_regression_hyperparams, imports,model_type)