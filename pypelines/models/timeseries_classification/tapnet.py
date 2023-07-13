from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

TapNet_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'dropout', 'min': 0, 'max': 1, 'step': 0.5},
    ],
    'categorical': [
        {'search': True, 'name': 'use_lstm', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_cnn', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_rp', 'selected': ['True'], 'values': ['True', 'False']},
        {'search': True, 'name': 'use_att', 'selected': ['True'], 'values': ['True', 'False']}
    ]
}


class TapNetTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'TapNetClassifier()'
        imports = '''from sktime.classification.deep_learning.tapnet import TapNetClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TapNetClassifier', model_string, TapNet_TS_classification_hyperparams, imports,model_type)

class TapNetTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'TapNetClassifier()'
        imports = '''from sktime.classification.deep_learning.tapnet import TapNetClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TapNetClassifier', model_string, TapNet_TS_classification_hyperparams, imports,model_type)