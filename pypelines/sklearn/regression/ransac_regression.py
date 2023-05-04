from ..model_base import SklearnModelBase,SklearnModelComparisonBase


ransac_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'max_trials', 'min': 10, 'max': 100, 'step': 10},
    ],
    'categorical': [
    ]
}

class RANSACRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'RANSACRegressor()'
        imports = '''from sklearn.linear_model import RANSACRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('ransac_regression', model_string, ransac_regression_hyperparams, imports,model_type)


class RANSACRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RANSACRegressor()'
        imports = '''from sklearn.linear_model import RANSACRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('ransac_regression', model_string, ransac_regression_hyperparams, imports,model_type)
