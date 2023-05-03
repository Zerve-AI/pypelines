from ..model_base import SklearnModelBase, SklearnModelComparisonBase

svc_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'C', 'min': 0.1, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'degree', 'min': 2, 'max': 5, 'step': 1},
    ],
    'categorical': [
        {'checked': True, 'name': 'kernel', 'selected': ['linear'], 'values': ['linear', 'rbf', 'sigmoid']},
        {'checked': False, 'name': 'gamma', 'selected': [], 'values': ['scale', 'auto']}
    ]
}


class SVCClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'SVC()'
        imports = '''from sklearn.svm import SVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('svc_classifier', model_string, svc_classification_hyperparams, imports,model_type)

class SVCClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'SVC()'
        imports = '''from sklearn.svm import SVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('svc_classifier', model_string, svc_classification_hyperparams, imports,model_type)