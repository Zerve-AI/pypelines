from ..model_base import SklearnModelBase,SklearnModelComparisonBase


quantile_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'quantile', 'min': 0, 'max': 1, 'step': 0.5},
        {'checked': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.5}        
    ],
    'categorical': [
        {'checked': True, 'name': 'solver', 'selected': ['interior-point'], 'values': ['highs-ds', 'highs-ipm', 'highs', 'interior-point', 'revised simplex']}
    ]
}

class QuantileRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'QuantileRegressor()'
        imports = '''from sklearn.linear_model import QuantileRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('quantile_regression', model_string, quantile_regression_hyperparams, imports,model_type)


class QuantileRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'QuantileRegressor()'
        imports = '''from sklearn.linear_model import QuantileRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('quantile_regression', model_string, quantile_regression_hyperparams, imports,model_type)
