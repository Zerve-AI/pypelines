from ..model_base import SklearnModelBase, SklearnModelComparisonBase

random_forest_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 20},
        {'search': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'search': True, 'name': 'min_samples_split', 'min': 0.5, 'max': 1, 'step': 0.1},
        {'search': True, 'name': 'min_samples_leaf', 'min': 1, 'max': 10, 'step': 2}
    ],
    'categorical': [
        {'search': False, 'name': 'criterion', 'selected': ['gini'], 'values': ['gini', 'entropy']},
        {'search': False, 'name': 'max_features', 'selected': ['auto'], 'values': ['auto', 'sqrt', 'log2']},
        {'search': False, 'name': 'bootstrap', 'selected': [True], 'values': [True, False]},
        {'search': False, 'name': 'oob_score', 'selected': [True], 'values': [True, False]},
        {'search': False, 'name': 'warm_start', 'selected': [False], 'values': [True, False]},
        {'search': False, 'name': 'class_weight', 'selected': ['balanced'], 'values': ['balanced', 'balanced_subsample']}
    ]
}

class RandomForestClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'RandomForestClassifier()'
        imports = '''from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('random_forest_classifier', model_string, random_forest_classification_hyperparams, imports, model_type)


class RandomForestClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'RandomForestClassifier()'
        imports = '''from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('random_forest_classifier', model_string, random_forest_classification_hyperparams, imports, model_type)