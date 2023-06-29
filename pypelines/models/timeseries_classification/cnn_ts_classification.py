from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

CNN_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'kernel_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'avg_pool_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'n_conv_layers', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'n_conv_layers', 'min': 4, 'max': 16, 'step': 4},
    ],
    'categorical': [
        
    ]
}


class CNNTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'CNNClassifier()'
        imports = '''from sktime.classification.deep_learning.cnn import CNNClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('CNNClassifier', model_string, CNN_TS_classification_hyperparams, imports,model_type)

class CNNTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'CNNClassifier()'
        imports = '''from sktime.classification.deep_learning.cnn import CNNClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('CNNClassifier', model_string, CNN_TS_classification_hyperparams, imports,model_type)