from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ShapeDTW_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_neighbors', 'min': 1, 'max': 10, 'step': 5}
    ],
    'categorical': [
        {'search': True, 'name': 'shape_descriptor_function', 'selected': ['raw'], 'values': ['raw','paa','dwt','slope','derivative','hog1d','compound']},
    ]
}


class ShapeDTWTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ShapeDTW()'
        imports = '''from sktime.classification.distance_based import ShapeDTW\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ShapeDTW', model_string, ShapeDTW_TS_classification_hyperparams, imports,model_type)

class ShapeDTWSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ShapeDTW()'
        imports = '''from sktime.classification.distance_based import ShapeDTW\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ShapeDTW', model_string, ShapeDTW_TS_classification_hyperparams, imports,model_type)