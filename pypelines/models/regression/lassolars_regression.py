from ..model_base import SklearnModelBase,SklearnModelComparisonBase


lassolars_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 2, 'step': 0.5},
        {'search': False, 'name': 'max_iter', 'min': 10, 'max': 500, 'step': 50}     
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]}
    ]
}

class LassoLarsRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'LassoLars()'
        imports = '''from sklearn.linear_model import LassoLars \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('lassolars_regression', model_string, lassolars_regression_hyperparams, imports,model_type)


class LassoLarsRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'LassoLars()'
        imports = '''from sklearn.linear_model import LassoLars \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('lassolars_regression', model_string, lassolars_regression_hyperparams, imports,model_type)
