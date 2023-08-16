from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

Signature_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'depth', 'min': 2, 'max': 4, 'step': 1}
    ],
    'categorical': [
        {'search': True, 'name': 'sig_tfm', 'selected': ['signature'], 'values':  ['signature', 'logsignature']}
    ]
}


class SignatureTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'SignatureClassifier()'
        imports = '''from sktime.classification.feature_based import SignatureClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SignatureClassifier', model_string, Signature_classification_hyperparams, imports,model_type)

class SignatureTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'SignatureClassifier()'
        imports = '''from sktime.classification.feature_based import SignatureClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SignatureClassifier', model_string, Signature_classification_hyperparams, imports,model_type)