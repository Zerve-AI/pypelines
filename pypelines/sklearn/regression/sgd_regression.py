from ..model_base import SklearnModelBase
from ..model_base import SklearnModelComparisonBase

sgd_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.5},
        {'checked': True, 'name': 'l1_ratio', 'min': 0.0, 'max': 1.0, 'step': 0.1},
        {'checked': True, 'name': 'max_iter', 'min': 500, 'max': 1000, 'step': 500},
        {'checked': True, 'name': 'epsilon', 'min': 0.001, 'max': 0.1, 'step': 0.05},

    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'early_stopping', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'shuffle', 'selected': [True], 'values': [True, False]}
    ]
}


class SGDRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'SGDRegressor()'
        imports = '''from sklearn.linear_model import SGDRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('sgd_regressor_regression', model_string, sgd_regression_hyperparams, imports,model_type)

class SGDRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'SGDRegressor()'
        imports = '''from sklearn.linear_model import SGDRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('sgd_regressor_regression', model_string, sgd_regression_hyperparams, imports,model_type)