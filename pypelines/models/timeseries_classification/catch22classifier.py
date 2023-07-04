from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

Catch22_classification_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'outlier_norm', 'selected': [False], 'values': [True, False]},
        {'search': True, 'name': 'replace_nans', 'selected': [True], 'values': [True, False]},
    ]
}


class Catch22TSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'Catch22Classifier()'
        imports = '''from sktime.classification.feature_based import Catch22Classifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('Catch22Classifier', model_string, Catch22_classification_hyperparams, imports,model_type)

class Catch22TSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'Catch22Classifier()'
        imports = '''from sktime.classification.feature_based import Catch22Classifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('Catch22Classifier', model_string, Catch22_classification_hyperparams, imports,model_type)