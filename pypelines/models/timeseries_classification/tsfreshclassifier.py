from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

TSFreshClassifier_classification_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'default_fc_parameters', 'selected': ['efficient'], 'values': ['efficient','minimal','comprehensive']}
    ]
}


class TSFreshTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'TSFreshClassifier()'
        imports = '''from sktime.classification.feature_based import TSFreshClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TSFreshClassifier', model_string, TSFreshClassifier_classification_hyperparams, imports,model_type)

class TSFreshTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'TSFreshClassifier()'
        imports = '''from sktime.classification.feature_based import TSFreshClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TSFreshClassifier', model_string, TSFreshClassifier_classification_hyperparams, imports,model_type)