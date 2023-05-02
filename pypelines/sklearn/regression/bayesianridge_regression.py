from ..model_base import SklearnModelBase,SklearnModelComparisonBase


bayesianridge_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_iter', 'min': 10, 'max': 300, 'step': 50}
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
        {'checked': True, 'name': 'compute_score', 'selected': [False], 'values': [True,False]},
        {'checked': True, 'name': 'copy_X', 'selected': [True], 'values': [True,False]}
    ]
}

class BayesianRidgeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'BayesianRidge()'
        imports = '''from sklearn.linear_model import BayesianRidge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('bayesian_ridge_regression', model_string, bayesianridge_regression_hyperparams, imports,model_type)


class BayesianRidgeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'BayesianRidge()'
        imports = '''from sklearn.linear_model import BayesianRidge \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('bayesian_ridge_regression', model_string, bayesianridge_regression_hyperparams, imports,model_type)