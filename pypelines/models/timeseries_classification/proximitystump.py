from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ProximityStump_TS_classification_hyperparams = {
}


class ProximityStumpTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ProximityStump()'
        imports = '''from sktime.classification.distance_based import ProximityStump\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityStump', model_string, ProximityStump_TS_classification_hyperparams, imports,model_type)

class ProximityStumpTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ProximityStump()'
        imports = '''from sktime.classification.distance_based import ProximityStump\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProximityStump', model_string, ProximityStump_TS_classification_hyperparams, imports,model_type)