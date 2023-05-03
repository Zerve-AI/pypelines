from ..model_base import SklearnModelBase,SklearnModelComparisonBase


extratree_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 10}
    ],
    'categorical': [
        {'checked': True, 'name': 'max_features', 'selected': [None], 'values': ["auto", "sqrt", "log2"]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'bootstrap', 'selected': [False], 'values': [True, False]}
    ]
}

class ExtraTreeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'ExtraTreesRegressor()'
        imports = '''from sklearn.ensemble import ExtraTreesRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('extra_tree_regression', model_string, extratree_regression_hyperparams, imports,model_type)


class ExtraTreeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ExtraTreesRegressor()'
        imports = '''from sklearn.ensemble import ExtraTreesRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('extra_tree_regression', model_string, extratree_regression_hyperparams, imports,model_type)
