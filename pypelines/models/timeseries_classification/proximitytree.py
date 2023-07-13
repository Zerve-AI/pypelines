from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ProximityTree_TS_classification_hyperparams = {
}


class ProximityTreeTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ProximityTree()'
        imports = '''from sktime.classification.distance_based import ProximityTree\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityTree', model_string, ProximityTree_TS_classification_hyperparams, imports,model_type)

class ProximityTreeTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ProximityTree()'
        imports = '''from sktime.classification.distance_based import ProximityTree\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityTree', model_string, ProximityTree_TS_classification_hyperparams, imports,model_type)