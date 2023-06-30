from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

MLP_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
    ],
    'categorical': [
        {'search': True, 'name': 'activation', 'selected': ['sigmoid'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
    ]
}


class MLPTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'MLPClassifier()'
        imports = '''from sktime.classification.deep_learning.mlp import MLPClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MLPClassifier', model_string, MLP_TS_classification_hyperparams, imports,model_type)

class MLPTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'MLPClassifier()'
        imports = '''from sktime.classification.deep_learning.mlp import MLPClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MLPClassifier', model_string, MLP_TS_classification_hyperparams, imports,model_type)