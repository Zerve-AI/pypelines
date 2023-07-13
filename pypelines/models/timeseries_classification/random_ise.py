from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

RandomISE_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20},
        {'search': False, 'name': 'min_interval', 'min': 4, 'max': 16, 'step': 4}
    ]
}


class RandomISETSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'RandomIntervalSpectralEnsemble()'
        imports = '''from sktime.classification.interval_based import RandomIntervalSpectralEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RandomIntervalSpectralEnsemble', model_string, RandomISE_classification_hyperparams, imports,model_type)

class RandomISETSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'RandomIntervalSpectralEnsemble()'
        imports = '''from sktime.classification.interval_based import RandomIntervalSpectralEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RandomIntervalSpectralEnsemble', model_string, RandomISE_classification_hyperparams, imports,model_type)