from ..model_base import SklearnModelBase, SklearnModelComparisonBase

mlp_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'hidden_layer_sizes', 'min': 10, 'max': 100, 'step': 10},
        {'checked': True, 'name': 'batch_size', 'min': 64, 'max': 512, 'step': 128},
        {'checked': True, 'name': 'learning_rate', 'min': 0.001, 'max': 0.1, 'step': 0.05},
    ],
    'categorical': [
        {'checked': True, 'name': 'learning_rate_init', 'selected': ['constant'],  'value': ['constant', 'invscaling', 'adaptive']},
        {'checked': True, 'name': 'solver', 'selected': ['adam'], 'value': ['lbfgs', 'sgd', 'adam']},
        {'checked': True, 'name': 'activation', 'selected': ['relu'], 'value': ['relu', 'identity', 'logistic', 'tanh']},
        {'checked': True, 'name': 'shuffle', 'selected': [True], 'value': [True, False]},
    ]
}


class MLPClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'MLPClassifier()'
        imports = '''from sklearn.neural_network import MLPClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('mlp_classifier', model_string, mlp_classification_hyperparams, imports,model_type)

class MLPClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'MLPClassifier()'
        imports = '''from sklearn.neural_network import MLPClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('mlp_classifier', model_string, mlp_classification_hyperparams, imports,model_type)