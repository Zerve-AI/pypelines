from ..model_base import SklearnModelBase,SklearnModelComparisonBase


bayesianridge_regression_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'n_iter', 'min': 10, 'max': 300, 'step': 50},
        {'search': False, 'name': 'alpha_1', 'min': 0.000001, 'max': 0.1, 'step': 0.005},
        {'search': False, 'name': 'alpha_2', 'min': 0.000001, 'max': 0.1, 'step': 0.005},
        {'search': False, 'name': 'lambda_1', 'min': 0.000001, 'max': 0.1, 'step': 0.005},
        {'search': False, 'name': 'lambda_2', 'min': 0.000001, 'max': 0.1, 'step': 0.005},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
        {'search': False, 'name': 'compute_score', 'selected': [False], 'values': [True,False]},
    ]
}

class BayesianRidgeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'BayesianRidge()'
        imports = '''from sklearn.linear_model import BayesianRidge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('bayesian_ridge_regression', model_string, bayesianridge_regression_hyperparams, imports,model_type)


class BayesianRidgeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'BayesianRidge()'
        imports = '''from sklearn.linear_model import BayesianRidge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('bayesian_ridge_regression', model_string, bayesianridge_regression_hyperparams, imports,model_type)
