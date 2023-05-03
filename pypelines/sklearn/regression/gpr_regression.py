from ..model_base import SklearnModelBase,SklearnModelComparisonBase


GPR_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 1e-10, 'max': 1e-10, 'step': 1e-10}
    ],
    'categorical': [
        {'checked': True, 'name': 'optimizer', 'selected': [None], 'values': [None, "fmin_l_bfgs_b"]},
        {'checked': True, 'name': 'normalize_y', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'copy_X_train', 'selected': [True], 'values': [True, False]}
    ]
}

class GPRRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'GaussianProcessRegressor()'
        imports = '''from sklearn.gaussian_process import GaussianProcessRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('gpr_regression', model_string, GPR_regression_hyperparams, imports,model_type)


class GPRRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GaussianProcessRegressor()'
        imports = '''from sklearn.gaussian_process import GaussianProcessRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('gpr_regression', model_string, GPR_regression_hyperparams, imports,model_type)
