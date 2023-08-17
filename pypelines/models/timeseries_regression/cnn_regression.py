from ..model_base import TSRegressionModelBase,TSRegressionModelComparisonBase

CNN_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'kernel_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'avg_pool_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'n_conv_layers', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'n_conv_layers', 'min': 4, 'max': 16, 'step': 4},
    ],
    'categorical': [
        
    ]
}


class CNNTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'CNNRegressor()'
        imports = '''from sktime.regression.deep_learning.cnn import CNNRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('CNNRegressor', model_string, CNN_TS_regression_hyperparams, imports,model_type)

class CNNTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'CNNRegressor()'
        imports = '''from sktime.regression.deep_learning.cnn import CNNRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('CNNRegressor', model_string, CNN_TS_regression_hyperparams, imports,model_type)