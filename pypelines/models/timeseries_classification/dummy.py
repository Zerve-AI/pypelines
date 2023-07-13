from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

DUMMY_TS_classification_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': True, 'name': 'strategy', 'selected': ['prior'], 'values': ['most_frequent', 'prior', 'stratified', 'uniform', 'constant']},
    ]
}


class DUMMYTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'DummyClassifier()'
        imports = '''from sktime.classification.dummy import DummyClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('DummyClassifier', model_string, DUMMY_TS_classification_hyperparams, imports,model_type)

class DUMMYTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'DummyClassifier()'
        imports = '''from sktime.classification.dummy import DummyClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('DummyClassifier', model_string, DUMMY_TS_classification_hyperparams, imports,model_type)