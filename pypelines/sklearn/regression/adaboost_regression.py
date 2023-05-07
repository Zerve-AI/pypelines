from ..model_base import SklearnModelBase,SklearnModelComparisonBase


adaboost_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 20}
    ],
    'categorical': [
        {'search': False, 'name': 'loss', 'selected': ["linear"], 'values': ["linear", "square", "exponential"]}
    ]
}

class AdaBoostRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'AdaBoostRegressor()'
        imports = '''from sklearn.ensemble import AdaBoostRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('adaboost_regression', model_string, adaboost_regression_hyperparams, imports,model_type)


class AdaBoostRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'AdaBoostRegressor()'
        imports = '''from sklearn.ensemble import AdaBoostRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('adaboost_regression', model_string, adaboost_regression_hyperparams, imports,model_type)
