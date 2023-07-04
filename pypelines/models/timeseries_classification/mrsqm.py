from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

MrSQM_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'features_per_rep', 'min': 100, 'max': 500, 'step': 50},
        {'search': False, 'name': 'selection_per_rep', 'min': 500, 'max': 2000, 'step': 200}
    ],
    'categorical': [
        {'search': True, 'name': 'sfa_norm', 'selected': [False], 'values': [True, False]}
    ]
}


class MrSQMTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'MrSQM()'
        imports = '''from sktime.classification.shapelet_based import MrSQM\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MrSQM', model_string, MrSQM_classification_hyperparams, imports,model_type)

class MrSQMTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'MrSQM()'
        imports = '''from sktime.classification.shapelet_based import MrSQM\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MrSQM', model_string, MrSQM_classification_hyperparams, imports,model_type)