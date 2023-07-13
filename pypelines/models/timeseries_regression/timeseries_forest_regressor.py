from ..model_base import TSRegressionModelBase, TSRegressionModelComparisonBase

TimeSeriesForestRegressor_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20},
        {'search': False, 'name': 'min_interval', 'min': 1, 'max': 3, 'step': 1}
    ]
}

class TimeSeriesForestTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'TimeSeriesForestRegressor()'
        imports = '''from sktime.regression.interval_based import TimeSeriesForestRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('TimeSeriesForestRegressor', model_string, TimeSeriesForestRegressor_hyperparams, imports,model_type)

class TimeSeriesForestTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesForestRegressor()'
        imports = '''from sktime.regression.interval_based import TimeSeriesForestRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Regression'
        super().__init__('TimeSeriesForestRegressor', model_string, TimeSeriesForestRegressor_hyperparams, imports,model_type)