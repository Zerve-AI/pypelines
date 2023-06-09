from ..model_base import SklearnModelBase,SklearnModelComparisonBase

ridge_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 10, 'max': 100, 'step': 10},
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'search': False, 'name': 'positive', 'selected': [True], 'values': [True, False]}
    ]
}


class RidgeClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'RidgeClassifier()'
        imports = '''from sklearn.linear_model import RidgeClassifier \nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ridge_classifer', model_string, ridge_classification_hyperparams, imports,model_type)

class RidgeClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RidgeClassifier()'
        imports = '''from sklearn.linear_model import RidgeClassifier \nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ridge_classifer', model_string, ridge_classification_hyperparams, imports,model_type)