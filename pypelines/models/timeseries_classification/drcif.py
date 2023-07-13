from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

DrCIF_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20},
        {'search': False, 'name': 'att_subsample_size', 'min': 5, 'max': 10, 'step': 2}
    ],
    'categorical': [
        {'search': True, 'name': 'save_transformed_data', 'selected': [False], 'values': [True, False]}
    ]
}


class DrCIFTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'DrCIF()'
        imports = '''from sktime.classification.interval_based import DrCIF\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('DrCIF', model_string, DrCIF_classification_hyperparams, imports,model_type)

class DrCIFTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'DrCIF()'
        imports = '''from sktime.classification.interval_based import DrCIF\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('DrCIF', model_string, DrCIF_classification_hyperparams, imports,model_type)