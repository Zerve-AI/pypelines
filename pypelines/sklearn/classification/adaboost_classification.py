from ..model_base import SklearnModelBase, SklearnModelComparisonBase

adaboost_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'learning_rate', 'min': 0, 'max': 1, 'step': 0.1},
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 10000, 'step': 1000},
    ],
    'categorical': [
        {'search': False, 'name': 'algorithm', 'selected': ['SAMME.R'], 'values': ['SAMME', 'SAMME.R']},
    ]
}


class ADABoostClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'AdaBoostClassifier()'
        imports = '''from sklearn.ensemble import AdaBoostClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('adaboost_classifier', model_string, adaboost_classification_hyperparams, imports,model_type)

class ADABoostClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'AdaBoostClassifier()'
        imports = '''from sklearn.ensemble import AdaBoostClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('adaboost_classifier', model_string, adaboost_classification_hyperparams, imports,model_type)