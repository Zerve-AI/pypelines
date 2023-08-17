from ..model_base import TSRegressionModelBase,TSRegressionModelComparisonBase

KNN_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_neighbors', 'min': 1, 'max': 10, 'step': 2}
    ],
    'categorical': [
        {'search': True, 'name': 'distance', 'selected': ['euclidean'], 'values': ['euclidean', 'dtw', 'wdtw','squared',
                                                                                            'ddtw', 'dwdtw', 'lcss',
                                                                                            'erp','wddtw', 'msm', 'twe']},
        {'search': True, 'name': 'weights', 'selected': ['uniform'], 'values': ['uniform', 'distance']},
        {'search': True, 'name': 'algorithm', 'selected': ['brute'], 'values': ['auto', 'ball_tree', 'kd_tree', 'brute']}
    ]
}


class KNNTSRegression(TSRegressionModelBase):
    def __init__(self):
        model_string = 'KNeighborsTimeSeriesRegressor()'
        imports = '''from sktime.regression.distance_based import KNeighborsTimeSeriesRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('KNeighborsTimeSeriesRegressor', model_string, KNN_TS_regression_hyperparams, imports,model_type)

class KNNTSRegressionComparison(TSRegressionModelComparisonBase):
    def __init__(self):
        model_string = 'KNeighborsTimeSeriesRegressor()'
        imports = '''from sktime.regression.distance_based import KNeighborsTimeSeriesRegressor\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('KNeighborsTimeSeriesRegressor', model_string, KNN_TS_regression_hyperparams, imports,model_type)
