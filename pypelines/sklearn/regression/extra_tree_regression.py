from ..model_base import SklearnModelBase,SklearnModelComparisonBase


extratree_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 10, 'max': 200, 'step': 50},
        {'search': True, 'name': 'max_depth', 'min': 10, 'max': 200, 'step': 50},
        {'search': False, 'name': 'min_samples_split', 'min': 2, 'max': 200, 'step': 50},
        {'search': False, 'name': 'min_samples_leaf', 'min': 0.1, 'max': 0.5, 'step': 0.1},
    ],
    'categorical': [
        {'search': False, 'name': 'max_features', 'selected': ['auto'], 'values': ["auto", "sqrt", "log2"]},
        {'search': False, 'name': 'bootstrap', 'selected': [True], 'values': [True, False]}
    ]
}

class ExtraTreeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'ExtraTreesRegressor()'
        imports = '''from sklearn.ensemble import ExtraTreesRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('extra_tree_regression', model_string, extratree_regression_hyperparams, imports,model_type)


class ExtraTreeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ExtraTreesRegressor()'
        imports = '''from sklearn.ensemble import ExtraTreesRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('extra_tree_regression', model_string, extratree_regression_hyperparams, imports,model_type)
