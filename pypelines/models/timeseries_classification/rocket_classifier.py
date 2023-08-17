from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

Rocket_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'num_kernels', 'min': 1000, 'max': 10000, 'step': 2000},
        {'search': False, 'name': 'n_features_per_kernel', 'min': 2, 'max': 4, 'step': 1}
    ],
    'categorical': [
        {'search': True, 'name': 'rocket_transform', 'selected': ['rocket'], 'values': ['rocket', 'minirocket', 'multirocket']}
    ]
}


class RocketTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'RocketClassifier()'
        imports = '''from sktime.classification.kernel_based import RocketClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RocketClassifier', model_string, Rocket_classification_hyperparams, imports,model_type)

class RocketTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'RocketClassifier()'
        imports = '''from sktime.classification.kernel_based import RocketClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RocketClassifier', model_string, Rocket_classification_hyperparams, imports,model_type)