from ..model_base import SklearnModelBase,SklearnModelComparisonBase



lasso_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 10, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'precompute', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'positive', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'selection', 'selected': ['cyclic'], 'values': ['cyclic', 'random']}
    ]
}


class Lasso(SklearnModelBase):
    def __init__(self):
        model_string = 'Lasso()'
        imports = '''from sklearn.linear_model import Lasso\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lasso', model_string, lasso_hyperparams, imports,model_type)

class LassoComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Lasso()'
        imports = '''from sklearn.linear_model import Lasso\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lasso', model_string, lasso_hyperparams, imports,model_type)