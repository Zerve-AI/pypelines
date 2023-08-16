from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ProximityForest_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 20},
        {'search': True, 'name': 'max_depth', 'min': 10, 'max': 20, 'step': 5}   
    ],
    'categorical': [
    ]
}


class ProximityForestTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ProximityForest()'
        imports = '''from sktime.classification.distance_based import ProximityForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityForest', model_string, ProximityForest_TS_classification_hyperparams, imports,model_type)

class ProximityForestTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ProximityForest()'
        imports = '''from sktime.classification.distance_based import ProximityForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityForest', model_string, ProximityForest_TS_classification_hyperparams, imports,model_type)