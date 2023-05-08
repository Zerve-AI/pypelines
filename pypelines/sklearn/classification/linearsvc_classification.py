from ..model_base import SklearnModelBase, SklearnModelComparisonBase

linearsvc_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'C', 'min': 0.1, 'max': 1, 'step': 0.2},
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 10000, 'step': 1000},
    ],
    'categorical': [
        {'search': True, 'name': 'penalty', 'selected': ['l2'], 'values': ['l1','l2']},
        {'search': False, 'name': 'loss', 'selected': ['squared_hinge'], 'values': ['hinge', 'squared_hinge']},
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]}
    ]
}


class LinearSVCClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'LinearSVC()'
        imports = '''from sklearn.svm import LinearSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('linearsvc_classifier', model_string, linearsvc_classification_hyperparams, imports,model_type)

class LinearSVCClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'LinearSVC()'
        imports = '''from sklearn.svm import LinearSVC\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('linearsvc_classifier', model_string, linearsvc_classification_hyperparams, imports,model_type)