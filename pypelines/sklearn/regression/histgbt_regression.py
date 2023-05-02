from ..model_base import SklearnModelBase
from ..model_base import SklearnModelComparisonBase

histogram_GBT_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'max_iter', 'min':10, 'max': 100, 'step':5},
        {'checked': True, 'name': 'max_leaf_nodes', 'min': 2, 'max': 31, 'step': 6},
        {'checked': True, 'name': 'min_samples_leaf', 'min':2, 'max': 20, 'step': 5},
        {'checked': True, 'name': 'max_bins', 'min': 25, 'max': 255, 'step': 25}
    ],
    'categorical': [
        {'checked': True, 'name': 'early_stopping', 'selected': [False], 'values': ['auto',True, False]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]}
    ]
}


class HistGBTRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'HistoGBTRegressor()'
        imports = '''from sklearn.ensemble import HistGradientBoostingRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('hist_gbt_regression', model_string, histogram_GBT_regression_hyperparams, imports,model_type)

class HistGBTRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'HistoGBTRegressor()'
        imports = '''from sklearn.ensemble import HistGradientBoostingRegressor\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('hist_gbt_regression', model_string, histogram_GBT_regression_hyperparams, imports,model_type)