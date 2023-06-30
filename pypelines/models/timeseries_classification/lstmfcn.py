from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

LSTMFCN_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'dropout', 'min': 4, 'max': 16, 'step': 4}
    ],
    'categorical': [
        
    ]
}


class LSTMFCNTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'LSTMFCNClassifier()'
        imports = '''from sktime.classification.deep_learning.lstmfcn import LSTMFCNClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('LSTMFCNClassifier', model_string, LSTMFCN_TS_classification_hyperparams, imports,model_type)

class LSTMFCNTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'LSTMFCNClassifier()'
        imports = '''from sktime.classification.deep_learning.lstmfcn import LSTMFCNClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('LSTMFCNClassifier', model_string, LSTMFCN_TS_classification_hyperparams, imports,model_type)