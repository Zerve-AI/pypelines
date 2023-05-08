from ..model_base import SklearnModelBase
from ..model_base import SklearnModelComparisonBase

histogram_GBT_regression_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'max_iter', 'min':10, 'max': 100, 'step':5},
        {'search': True, 'name': 'max_leaf_nodes', 'min': 2, 'max': 100, 'step': 35},
        {'search': True, 'name': 'min_samples_leaf', 'min':10, 'max': 100, 'step': 40},
        {'search': False, 'name': 'max_depth', 'min':1, 'max': 10, 'step': 3},
        {'search': False, 'name': 'l2_regularization', 'min':0, 'max': 2, 'step':0.5},
        {'search': True, 'name': 'max_bins', 'min': 25, 'max': 255, 'step': 100},
        {'search': False, 'name': 'learning_rate', 'min': 0.1, 'max': 0.5, 'step': 0.1},
    ],
    'categorical': [
        {'search': False, 'name': 'early_stopping', 'selected': [True], 'values': ['auto',True, False]},
    ]
}


class HistGBTRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'HistGradientBoostingRegressor()'
        imports = '''from sklearn.ensemble import HistGradientBoostingRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('hist_gbt_regression', model_string, histogram_GBT_regression_hyperparams, imports,model_type)

class HistGBTRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'HistGradientBoostingRegressor()'
        imports = '''from sklearn.ensemble import HistGradientBoostingRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('hist_gbt_regression', model_string, histogram_GBT_regression_hyperparams, imports,model_type)