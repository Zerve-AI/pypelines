from ..model_base import SklearnModelBase, SklearnModelComparisonBase

nusvc_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'nu', 'min': 0.1, 'max': 1, 'step': 0.2},
        {'search': True, 'name': 'degree', 'min': 2, 'max': 5, 'step': 1},
    ],
    'categorical': [
        {'search': True, 'name': 'kernel', 'selected': ['poly'], 'values': ['linear', 'rbf', 'sigmoid','poly','sigmoid']},
        {'search': False, 'name': 'gamma', 'selected': ['scale'], 'values': ['scale', 'auto']},
        {'search': True, 'name': 'probability', 'selected': [True], 'values': [True]}
    ]
}


class NuSVCClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'NuSVC()'
        imports = '''from sklearn.svm import NuSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('nusvc_classifier', model_string, nusvc_classification_hyperparams, imports,model_type)

class NuSVCClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'NuSVC()'
        imports = '''from sklearn.svm import NuSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('nusvc_classifier', model_string, nusvc_classification_hyperparams, imports,model_type)