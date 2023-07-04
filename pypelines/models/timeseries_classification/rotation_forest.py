from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

RotationForest_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20},
        {'search': False, 'name': 'min_group', 'min': 1, 'max': 3, 'step': 1},
        {'search': False, 'name': 'max_group', 'min': 1, 'max': 3, 'step': 1},
    ],
    'categorical': [
        {'search': True, 'name': 'save_transformed_data', 'selected': ['False'], 'values': ['True', 'False']}
    ]
}


class RotationForestTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'RotationForest()'
        imports = '''from sktime.classification.sklearn import RotationForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RotationForest', model_string, RotationForest_classification_hyperparams, imports,model_type)

class RotationForestTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'RotationForest()'
        imports = '''from sktime.classification.sklearn import RotationForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RotationForest', model_string, RotationForest_classification_hyperparams, imports,model_type)