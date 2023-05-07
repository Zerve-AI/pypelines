from ..model_base import SklearnModelBase,SklearnModelComparisonBase


huber_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'epsilon', 'min': 1, 'max': 10, 'step': 2},
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 3, 'step': 0.5}
        
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]}        
    ]
}

class HuberRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'HuberRegressor()'
        imports = '''from sklearn.linear_model import HuberRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('huber_regression', model_string, huber_regression_hyperparams, imports,model_type)


class HuberRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'HuberRegressor()'
        imports = '''from sklearn.linear_model import HuberRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('huber_regression', model_string, huber_regression_hyperparams, imports,model_type)
