from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

RandomIC_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_intervals', 'min': 20, 'max': 100, 'step': 20}
    ]
}


class RandomICTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'RandomIntervalClassifier()'
        imports = '''from sktime.classification.feature_based import RandomIntervalClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RandomIntervalClassifier', model_string, RandomIC_TS_classification_hyperparams, imports,model_type)

class RandomICTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'RandomIntervalClassifier()'
        imports = '''from sktime.classification.feature_based import RandomIntervalClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('RandomIntervalClassifier', model_string, RandomIC_TS_classification_hyperparams, imports,model_type)