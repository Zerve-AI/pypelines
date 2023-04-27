from ..model_base import SklearnModelBase,SklearnModelComparisonBase

ridgeclassifier_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 10, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'max_iter', 'min': 100, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'positive', 'selected': [True], 'values': [True, False]}
    ]
}


class RidgeClassifier(SklearnModelBase):
    def __init__(self):
        model_string = 'RidgeClassifier()'
        imports = '''from sklearn.linear_model import RidgeClassifier \nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('ridge_classifer', model_string, ridgeclassifier_hyperparams, imports,model_type)

class RidgeClassifierComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RidgeClassifier()'
        imports = '''from sklearn.linear_model import RidgeClassifier \nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('ridge_classifer', model_string, ridgeclassifier_hyperparams, imports,model_type)