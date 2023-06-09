from ..model_base import SklearnModelBase, SklearnModelComparisonBase

histgbt_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'learning_rate', 'min': 0.1, 'max': 1, 'step': 0.1},
        {'search': True, 'name': 'max_iter', 'min': 1000, 'max': 10000, 'step': 1000},
    ],
    'categorical': [
    ]
}


class HistGBTClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'HistGradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import HistGradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('histgbt_classifier', model_string, histgbt_classification_hyperparams, imports,model_type)

class HistGBTClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'HistGradientBoostingClassifier()'
        imports = '''from sklearn.ensemble import HistGradientBoostingClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('histgbt_classifier', model_string, histgbt_classification_hyperparams, imports,model_type)