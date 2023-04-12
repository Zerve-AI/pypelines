from ..model_base import SklearnModelBase,SklearnModelComparisonBase


linear_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_jobs', 'min': 1, 'max': 10, 'step': 1},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': False, 'name': 'normalize', 'selected': [True], 'values': [True, False]},
    ]
}

class LinearRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'LinearRegression()'
        imports = '''from sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nfrom sklearn.metrics import r2_score as model_accuracy\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lin_reg', model_string, linear_regression_hyperparams, imports,model_type)


class LinearRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'LinearRegression()'
        imports = '''from sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nfrom sklearn.metrics import r2_score as model_accuracy\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('lin_reg', model_string, linear_regression_hyperparams, imports,model_type)
