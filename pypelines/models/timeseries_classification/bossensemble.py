from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

BOSSEnsemble_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'max_ensemble_size', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'max_win_len_prop', 'min': 0.1, 'max': 1, 'step': 0.5},
        {'search': False, 'name': 'min_window', 'min': 10, 'max': 100, 'step': 50},
    ],
    'categorical': [
        {'search': True, 'name': 'use_boss_distance', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'feature_selection', 'selected': ['none'], 'values': ['chi2', 'none', 'random']},
    ]
}


class BOSSEnsembleTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'BOSSEnsemble()'
        imports = '''from sktime.classification.dictionary_based import BOSSEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('BOSSEnsemble', model_string, BOSSEnsemble_TS_classification_hyperparams, imports,model_type)

class BOSSEnsembleTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'BOSSEnsemble()'
        imports = '''from sktime.classification.dictionary_based import BOSSEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('BOSSEnsemble', model_string, BOSSEnsemble_TS_classification_hyperparams, imports,model_type)