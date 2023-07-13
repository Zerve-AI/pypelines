from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

InceptionTime_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_epochs', 'min': 100, 'max': 2000, 'step': 1000},
        {'search': False, 'name': 'batch_size', 'min': 4, 'max': 16, 'step': 4},
        {'search': False, 'name': 'kernel_size', 'min': 40, 'max': 100, 'step': 20},
        {'search': False, 'name': 'n_filters', 'min': 32, 'max': 64, 'step': 16},
        {'search': False, 'name': 'bottleneck_size', 'min': 32, 'max': 64, 'step': 16}
    ],
    'categorical': [
    ]
}


class InceptionTimeClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'InceptionTimeClassifier()'
        imports = '''from sktime.classification.deep_learning.inceptiontime import InceptionTimeClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('InceptionTimeClassifier', model_string, InceptionTime_TS_classification_hyperparams, imports,model_type)

class InceptionTimeClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'InceptionTimeClassifier()'
        imports = '''from sktime.classification.deep_learning.inceptiontime import InceptionTimeClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('InceptionTimeClassifier', model_string, InceptionTime_TS_classification_hyperparams, imports,model_type)