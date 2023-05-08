from ..model_base import SklearnModelBase,SklearnModelComparisonBase


gamma_regression_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'max_iter', 'min': 10, 'max': 100, 'step': 10},      
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 2, 'step': 1}      
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]}        
    ]
}

class GammaRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'GammaRegressor()'
        imports = '''from sklearn.linear_model import GammaRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('gamma_regression', model_string, gamma_regression_hyperparams, imports,model_type)


class GammaRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GammaRegressor()'
        imports = '''from sklearn.linear_model import GammaRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('gamma_regression', model_string, gamma_regression_hyperparams, imports,model_type)
