from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

TimeSeriesForestClassifier_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20},
        {'search': False, 'name': 'min_interval', 'min': 1, 'max': 3, 'step': 1}
    ]
}

class TimeSeriesForestTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'TimeSeriesForestClassifier()'
        imports = '''from sktime.classification.interval_based import TimeSeriesForestClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TimeSeriesForestClassifier', model_string, TimeSeriesForestClassifier_classification_hyperparams, imports,model_type)

class TimeSeriesForestTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesForestClassifier()'
        imports = '''from sktime.classification.interval_based import TimeSeriesForestClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TimeSeriesForestClassifier', model_string, TimeSeriesForestClassifier_classification_hyperparams, imports,model_type)