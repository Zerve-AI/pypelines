from ..model_base import TSRegressionModelBase, TSRegressionModelComparisonBase

TapNet_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'dropout', 'min': 0, 'max': 1, 'step': 0.5},
    ],
    'categorical': [
        {'search': True, 'name': 'use_lstm', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_cnn', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_rp', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_att', 'selected': ['True'], 'values': ['True', 'False']}
    ]
}


class TapNetTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'TapNetRegressor()'
        imports = '''from sktime.regression.deep_learning.tapnet import TapNetRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TapNetRegressor', model_string, TapNet_TS_regression_hyperparams, imports,model_type)

class TapNetTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'TapNetRegressor()'
        imports = '''from sktime.regression.deep_learning.tapnet import TapNetRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TapNetRegressor', model_string, TapNet_TS_regression_hyperparams, imports,model_type)