from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

TimeSeriesSVC_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'cache_size', 'min': 100, 'max': 200, 'step': 20}
    ],
    'categorical': [
        {'search': True, 'name': 'probability', 'selected': [False], 'values': [True, False]}
    ]
}


class TimeSeriesSVCTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'TimeSeriesSVC()'
        imports = '''from sktime.classification.kernel_based import TimeSeriesSVC\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TimeSeriesSVC', model_string, TimeSeriesSVC_classification_hyperparams, imports,model_type)

class TimeSeriesSVCTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesSVC()'
        imports = '''from sktime.classification.kernel_based import TimeSeriesSVC\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TimeSeriesSVC', model_string, TimeSeriesSVC_classification_hyperparams, imports,model_type)