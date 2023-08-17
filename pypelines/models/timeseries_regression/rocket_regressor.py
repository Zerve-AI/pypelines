from ..model_base import TSRegressionModelBase, TSRegressionModelComparisonBase

Rocket_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'num_kernels', 'min': 1000, 'max': 10000, 'step': 2000},
        {'search': False, 'name': 'n_features_per_kernel', 'min': 2, 'max': 4, 'step': 1}
    ],
    'categorical': [
        {'search': True, 'name': 'rocket_transform', 'selected': ['rocket'], 'values': ['rocket', 'minirocket', 'multirocket']}
    ]
}


class RocketTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'RocketRegressor()'
        imports = '''from sktime.regression.kernel_based import RocketRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('RocketRegressor', model_string, Rocket_TS_regression_hyperparams, imports,model_type)

class RocketTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'RocketRegressor()'
        imports = '''from sktime.regression.kernel_based import RocketRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('RocketRegressor', model_string, Rocket_TS_regression_hyperparams, imports,model_type)