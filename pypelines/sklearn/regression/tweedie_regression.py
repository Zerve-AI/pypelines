from ..model_base import SklearnModelBase,SklearnModelComparisonBase


tweedie_regression_hyperparams = {
    'numerical': [
        {'checked': False, 'name': 'max_iter', 'min': 10, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'power', 'min': 0, 'max': 3, 'step': 1},          
        {'checked': True, 'name': 'alpha', 'min': 0, 'max': 5, 'step': 1}          
    ],
    'categorical': [
        {'checked': False, 'name': 'link', 'selected': ['auto'], 'values': ['auto', 'log', 'identity']},
        {'checked': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]}        
    ]
}

class TweedieRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'TweedieRegressor()'
        imports = '''from sklearn.linear_model import TweedieRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('tweedie_regression', model_string, tweedie_regression_hyperparams, imports,model_type)


class TweedieRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'TweedieRegressor()'
        imports = '''from sklearn.linear_model import TweedieRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('tweedie_regression', model_string, tweedie_regression_hyperparams, imports,model_type)
