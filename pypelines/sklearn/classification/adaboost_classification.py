from ..model_base import SklearnModelBase, SklearnModelComparisonBase

adaboost_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'learning_rate', 'min': 0, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'n_estimators', 'min': 100, 'max': 10000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'algorithm', 'selected': ['SAMME.R'], 'values': ['SAMME', 'SAMME.R']},
    ]
}


class ADABoostClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'ADABoostClassifier()'
        imports = '''from sklearn.ensemble import AdaBoostClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('adaboost_classifier', model_string, adaboost_classification_hyperparams, imports,model_type)

class ADABoostClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ADABoostClassifier()'
        imports = '''from sklearn.ensemble import AdaBoostClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('adaboost_classifier', model_string, adaboost_classification_hyperparams, imports,model_type)