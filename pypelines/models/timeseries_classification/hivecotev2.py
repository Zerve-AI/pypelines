from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

HIVECOTEV2_classification_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'save_component_probas', 'selected': [False], 'values': [True, False]}
    ]
}


class HIVECOTEV2TSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'HIVECOTEV2()'
        imports = '''from sktime.classification.hybrid import HIVECOTEV2\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('HIVECOTEV2', model_string, HIVECOTEV2_classification_hyperparams, imports,model_type)

class HIVECOTEV2TSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'HIVECOTEV2()'
        imports = '''from sktime.classification.hybrid import HIVECOTEV2\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('HIVECOTEV2', model_string, HIVECOTEV2_classification_hyperparams, imports,model_type)