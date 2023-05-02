from ..model_base import SklearnModelBase,SklearnModelComparisonBase


random_forest_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 5}
    ],
    'categorical': [
        {'checked': True, 'name': 'bootstrap', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]}
    ]
}

class RandomForestRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'RandomForestRegressor()'
        imports = '''from sklearn.ensemble import RandomForestRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('random_forest_regression', model_string, random_forest_regression_hyperparams, imports,model_type)


class RandomForestRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RandomForestRegressor()'
        imports = '''from sklearn.ensemble import RandomForestRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('random_forest_regression', model_string, random_forest_regression_hyperparams, imports,model_type)
