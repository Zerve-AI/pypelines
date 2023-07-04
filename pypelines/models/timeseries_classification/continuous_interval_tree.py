from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ContinuousIntervalTree_classification_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'thresholds', 'min': 10, 'max': 20, 'step': 5}
    ]
}


class ContinuousIntervalTreeTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ContinuousIntervalTree()'
        imports = '''from sktime.classification.sklearn import ContinuousIntervalTree\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ContinuousIntervalTree', model_string, ContinuousIntervalTree_classification_hyperparams, imports,model_type)

class ContinuousIntervalTreeTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ContinuousIntervalTree()'
        imports = '''from sktime.classification.sklearn import ContinuousIntervalTree\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ContinuousIntervalTree', model_string, ContinuousIntervalTree_classification_hyperparams, imports,model_type)