from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

HIVECOTEV1_classification_hyperparams = {
}


class HIVECOTEV1TSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'HIVECOTEV1()'
        imports = '''from sktime.classification.hybrid import HIVECOTEV1\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('HIVECOTEV1', model_string, HIVECOTEV1_classification_hyperparams, imports,model_type)

class HIVECOTEV1TSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'HIVECOTEV1()'
        imports = '''from sktime.classification.hybrid import HIVECOTEV1\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('HIVECOTEV1', model_string, HIVECOTEV1_classification_hyperparams, imports,model_type)