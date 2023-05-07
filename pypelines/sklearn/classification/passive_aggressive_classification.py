from ..model_base import SklearnModelBase, SklearnModelComparisonBase


passive_aggressive_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'C', 'min': 0.1, 'max': 1, 'step': 0.1},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values':  [True,False]},
        {'search': False, 'name': 'average', 'selected': [True], 'values': [True, False]},
    ]
}


class PassiveAggressiveClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'PassiveAggressiveClassifier()'
        imports = '''from sklearn.linear_model import PassiveAggressiveClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('passive_aggressive_classifier', model_string, passive_aggressive_classification_hyperparams, imports,model_type)

class PassiveAggressiveClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'PassiveAggressiveClassifier()'
        imports = '''from sklearn.linear_model import PassiveAggressiveClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('passive_aggressive_classifier', model_string, passive_aggressive_classification_hyperparams, imports,model_type)