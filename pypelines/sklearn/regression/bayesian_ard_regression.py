from ..model_base import SklearnModelBase,SklearnModelComparisonBase


ard_regression_hyperparams = {
    'numerical': [
        {'checked': False, 'name': 'n_iter', 'min': 10, 'max': 300, 'step': 50}
    ],
    'categorical': [
        {'checked': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
        {'checked': False, 'name': 'compute_score', 'selected': [False], 'values': [True,False]},
    ]
}

class ARDRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'ARDRegression()'
        imports = '''from sklearn.linear_model import ARDRegression \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('bayesian_ard_regression', model_string, ard_regression_hyperparams, imports,model_type)


class ARDRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ARDRegression()'
        imports = '''from sklearn.linear_model import ARDRegression \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('bayesian_ard_regression', model_string, ard_regression_hyperparams, imports,model_type)
