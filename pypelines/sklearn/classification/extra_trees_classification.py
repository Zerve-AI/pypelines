from ..model_base import SklearnModelBase, SklearnModelComparisonBase


extra_trees_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 500, 'step': 100},
        {'search': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'search': False, 'name': 'max_samples', 'min': 0.1, 'max': 1.0, 'step': 0.2},
    ],
    'categorical': [
        {'search': False, 'name': 'criterion', 'selected': ['gini'], 'values':  ['gini', 'entropy', 'log_loss']},
        {'search': False, 'name': 'max_features', 'selected': ['log2'], 'values': ['sqrt', 'log2', None]},
    ]
}


class ExtraTreesClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'ExtraTreesClassifier()'
        imports = '''from sklearn.ensemble import ExtraTreesClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('extra_trees_classifier', model_string, extra_trees_classification_hyperparams, imports,model_type)

class ExtraTreesClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ExtraTreesClassifier()'
        imports = '''from sklearn.ensemble import ExtraTreesClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('extra_trees_classifier', model_string, extra_trees_classification_hyperparams, imports,model_type)