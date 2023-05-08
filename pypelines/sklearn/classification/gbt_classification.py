from ..model_base import SklearnModelBase, SklearnModelComparisonBase

gbt_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'learning_rate', 'min': 0, 'max': 1, 'step': 0.2},
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 10000, 'step': 1000},
        {'search': True, 'name': 'subsample', 'min': 0.1, 'max': 1, 'step': 0.2},
        {'search': True, 'name': 'max_depth', 'min': 1, 'max': 10000, 'step': 1000},
    ],
    'categorical': [
    ]
}


class GBTClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'GradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('gbt_classifier', model_string, gbt_classification_hyperparams, imports,model_type)

class GBTClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('gbt_classifier', model_string, gbt_classification_hyperparams, imports,model_type)