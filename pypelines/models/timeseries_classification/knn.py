from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

KNN_TS_classification_hyperparams = {
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


class KNNTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'KNeighborsTimeSeriesClassifier()'
        imports = '''from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('KNeighborsTimeSeriesClassifier', model_string, KNN_TS_classification_hyperparams, imports,model_type)

class KNNTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'KNeighborsTimeSeriesClassifier()'
        imports = '''from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('KNeighborsTimeSeriesClassifier', model_string, KNN_TS_classification_hyperparams, imports,model_type)