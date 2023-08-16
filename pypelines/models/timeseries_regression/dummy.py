from ..model_base import TSRegressionModelBase,TSRegressionModelComparisonBase

DUMMY_TS_regression_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'strategy', 'selected': ['prior'], 'values': ['most_frequent', 'prior', 'stratified', 'uniform', 'constant']},
    ]
}


class DUMMYTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'DummyRegressor()'
        imports = '''from sktime.regression.dummy import DummyRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('DummyRegressor', model_string, DUMMY_TS_regression_hyperparams, imports,model_type)

class DUMMYTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'DummyRegressor()'
        imports = '''from sktime.regression.dummy import DummyRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('DummyRegressor', model_string, DUMMY_TS_regression_hyperparams, imports,model_type)