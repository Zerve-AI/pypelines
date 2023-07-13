from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

Arsenal_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'num_kernels', 'min': 500, 'max': 2000, 'step': 200},
        {'search': False, 'name': 'n_features_per_kernel', 'min': 2, 'max': 4, 'step': 1}
    ],
    'categorical': [
        {'search': True, 'name': 'save_transformed_data', 'selected': [False], 'values': [True, False]}
    ]
}


class ArsenalTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'Arsenal()'
        imports = '''from sktime.classification.kernel_based import Arsenal\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('Arsenal', model_string, Arsenal_classification_hyperparams, imports,model_type)

class ArsenalTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'Arsenal()'
        imports = '''from sktime.classification.kernel_based import Arsenal\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('Arsenal', model_string, Arsenal_classification_hyperparams, imports,model_type)