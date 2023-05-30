from ..model_base import SklearnModelBase, SklearnModelComparisonBase

svc_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'C', 'min': 0.1, 'max': 1, 'step': 0.2},
        {'search': True, 'name': 'degree', 'min': 2, 'max': 5, 'step': 1},
    ],
    'categorical': [
        {'search': True, 'name': 'kernel', 'selected': ['linear'], 'values': ['linear', 'rbf', 'sigmoid']},
        {'search': False, 'name': 'gamma', 'selected': ['scale'], 'values': ['scale', 'auto']},
        {'search': True, 'name': 'probability', 'selected': [True], 'values': [True]}
    ]
}


class SVCClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'SVC()'
        imports = '''from sklearn.svm import SVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('svc_classifier', model_string, svc_classification_hyperparams, imports,model_type)

class SVCClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'SVC()'
        imports = '''from sklearn.svm import SVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('svc_classifier', model_string, svc_classification_hyperparams, imports,model_type)