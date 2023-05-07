from ..model_base import SklearnModelBase,SklearnModelComparisonBase


gbt_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 25, 'max': 200, 'step': 50},
        {'search': True, 'name': 'max_depth', 'min': 1, 'max': 10, 'step': 3},
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.5},
        {'search': False, 'name': 'min_samples_split', 'min': 2, 'max': 200, 'step': 50},
        {'search': False, 'name': 'min_samples_leaf', 'min': 0.1, 'max': 1, 'step': 0.5},
    ],
    'categorical': [
        {'search': False, 'name': 'max_features', 'selected': ['auto'], 'values': ["auto", "sqrt", "log2"]},
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
