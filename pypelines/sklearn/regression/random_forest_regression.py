from ..model_base import SklearnModelBase,SklearnModelComparisonBase


random_forest_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 50, 'max': 150, 'step': 35},
        {'search': True, 'name': 'max_depth', 'min': 5, 'max': 50, 'step': 10},
        {'search': True, 'name': 'min_samples_leaf', 'min': 1, 'max': 50, 'step': 20}
    ],
    'categorical': [
        {'search': False, 'name': 'bootstrap', 'selected': [True], 'values': [True, False]},
    ]
}

class RandomForestRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'RandomForestRegressor()'
        imports = '''from sklearn.ensemble import RandomForestRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('random_forest_regression', model_string, random_forest_regression_hyperparams, imports,model_type)


class RandomForestRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RandomForestRegressor()'
        imports = '''from sklearn.ensemble import RandomForestRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('random_forest_regression', model_string, random_forest_regression_hyperparams, imports,model_type)
