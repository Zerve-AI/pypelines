from ..model_base import SklearnModelBase, SklearnModelComparisonBase

random_forest_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'n_estimators', 'min': 10, 'max': 100, 'step': 20},
        {'checked': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'checked': True, 'name': 'min_samples_split', 'min': 0.5, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'min_samples_leaf', 'min': 1, 'max': 10, 'step': 2}
    ],
    'categorical': [
        {'checked': True, 'name': 'criterion', 'selected': ['gini'], 'values': ['gini', 'entropy']},
        {'checked': True, 'name': 'max_features', 'selected': ['auto'], 'values': ['auto', 'sqrt', 'log2']},
        {'checked': True, 'name': 'bootstrap', 'selected': [True], 'values': [True, False]},
        {'checked': False, 'name': 'oob_score', 'selected': [], 'values': [True, False]},
        {'checked': False, 'name': 'warm_start', 'selected': [], 'values': [True, False]},
        {'checked': False, 'name': 'class_weight', 'selected': [], 'values': ['balanced', 'balanced_subsample']}
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