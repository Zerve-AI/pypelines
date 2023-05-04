from ..model_base import SklearnModelBase, SklearnModelComparisonBase

nusvc_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'nu', 'min': 0.1, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'degree', 'min': 2, 'max': 5, 'step': 1},
    ],
    'categorical': [
        {'checked': True, 'name': 'kernel', 'selected': ['poly'], 'values': ['linear', 'rbf', 'sigmoid','poly','sigmoid']},
        {'checked': False, 'name': 'gamma', 'selected': ['scale'], 'values': ['scale', 'auto']}
    ]
}


class NuSVCClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'NuSVC()'
        imports = '''from sklearn.svm import NuSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('nusvc_classifier', model_string, nusvc_classification_hyperparams, imports,model_type)

class NuSVCClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'NuSVC()'
        imports = '''from sklearn.svm import NuSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('nusvc_classifier', model_string, nusvc_classification_hyperparams, imports,model_type)