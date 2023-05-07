from ..model_base import SklearnModelBase, SklearnModelComparisonBase

decision_tree_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'search': True, 'name': 'min_samples_split', 'min': 2, 'max': 10, 'step': 2},
        {'search': True, 'name': 'min_samples_leaf', 'min': 1, 'max': 10, 'step': 5},
        {'search': True, 'name': 'min_weight_fraction_leaf', 'min': 0.0, 'max': 0.5, 'step': 0.25},
        {'search': True, 'name': 'max_leaf_nodes', 'min': 1, 'max': 10, 'step': 5},
        {'search': True, 'name': 'min_impurity_decrease', 'min': 0.0, 'max': 0.5, 'step': 0.25}
    ],
    'categorical': [
        {'search': False, 'name': 'criterion', 'selected': ['gini'], 'values': ['gini', 'entropy']},
        {'search': False, 'name': 'splitter', 'selected': ['best'], 'values': ['best', 'random']},
        {'search': False, 'name': 'max_features', 'selected': ['auto'], 'values': ['auto', 'sqrt', 'log2']},
    ]
}


class DecisionTreeClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'DecisionTreeClassifier()'
        imports = '''from sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('dt_classifier', model_string, decision_tree_classification_hyperparams, imports,model_type)

class DecisionTreeClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'DecisionTreeClassifier()'
        imports = '''from sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('dt_classifier', model_string, decision_tree_classification_hyperparams, imports,model_type)