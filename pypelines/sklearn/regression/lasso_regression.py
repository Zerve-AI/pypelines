from ..model_base import SklearnModelBase,SklearnModelComparisonBase



lasso_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 2, 'step': .5},
        {'search': False, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
    ]
}


class LassoRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'Lasso()'
        imports = '''from sklearn.linear_model import Lasso\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lasso_regression', model_string, lasso_regression_hyperparams, imports,model_type)    

class LassoRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Lasso()'
        imports = '''from sklearn.linear_model import Lasso\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lasso_regression', model_string, lasso_regression_hyperparams, imports,model_type)