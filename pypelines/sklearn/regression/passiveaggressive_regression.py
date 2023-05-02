from ..model_base import SklearnModelBase,SklearnModelComparisonBase


passiveaggressive_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'C', 'min': 0, 'max': 1, 'step': 0.5},
        {'checked': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100}        
    ],
    'categorical': [
        {'checked': True, 'name': 'early_stopping', 'selected': [False], 'values': [True,False]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True,False]},
        {'checked': True, 'name': 'early_stopping', 'selected': [False], 'values': [True,False]},
    ]
}

class PassiveAggressiveRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'PassiveAggressiveRegressor()'
        imports = '''from sklearn.linear_model import PassiveAggressiveRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('passiveaggressive_regression', model_string, passiveaggressive_regression_hyperparams, imports,model_type)


class PassiveAggressiveRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'PassiveAggressiveRegressor()'
        imports = '''from sklearn.linear_model import PassiveAggressiveRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('passiveaggressive_regression', model_string, passiveaggressive_regression_hyperparams, imports,model_type)
