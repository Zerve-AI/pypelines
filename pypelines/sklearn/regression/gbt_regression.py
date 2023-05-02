from ..model_base import SklearnModelBase,SklearnModelComparisonBase


gbt_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_estimators', 'min': 1, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'max_depth', 'min': 1, 'max': 3, 'step': 1},
        {'checked': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.5},
    ],
    'categorical': [
        {'checked': True, 'name': 'max_features', 'selected': [None], 'values': ["auto", "sqrt", "log2"]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]}
    ]
}

class GBTRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'GradientBoostingRegressor()'
        imports = '''from sklearn.ensemble import GradientBoostingRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('gbt_regression', model_string, gbt_regression_hyperparams, imports,model_type)


class GBTRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GradientBoostingRegressor()'
        imports = '''from sklearn.ensemble import GradientBoostingRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('gbt_regression', model_string, gbt_regression_hyperparams, imports,model_type)
