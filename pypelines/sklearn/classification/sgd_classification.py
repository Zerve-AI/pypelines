from ..model_base import SklearnModelBase, SklearnModelComparisonBase

sgd_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'max_iter', 'min': 1, 'max': 1000, 'step': 10},
    ],
    'categorical': [
        {'checked': True, 'name': 'loss', 'selected': ['hinge'], 'values': ['hinge', 'log_loss', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_error', 'huber', 'epsilon_insensitive', 'squared_epsilon_insensitive']},
        {'checked': True, 'name': 'penalty', 'selected': ['l2'], 'values': ['l2', 'l1', 'elasticnet']},
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
        {'checked': True, 'name': 'shuffle', 'selected': [True], 'values': [True,False]},
        {'checked': True, 'name': 'learning_rate', 'selected': ['optimal'], 'values': ['constant','optimal','invscaling','adaptive']},
        {'checked': True, 'name': 'average', 'selected': [True], 'values': [True,False]},
    ]
}


class SGDClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'SGDClassifier()'
        imports = '''from sklearn.linear_model import SGDClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('sgd_classifier', model_string, sgd_classification_hyperparams, imports,model_type)

class SGDClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'SGDClassifier()'
        imports = '''from sklearn.linear_model import SGDClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('sgd_classifier', model_string, sgd_classification_hyperparams, imports,model_type)