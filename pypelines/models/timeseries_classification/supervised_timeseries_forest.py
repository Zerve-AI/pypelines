from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

SupervisedTimeSeriesForest_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 200, 'step': 20}
    ]
}

class SupervisedTimeSeriesForestTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'SupervisedTimeSeriesForest()'
        imports = '''from sktime.classification.interval_based import SupervisedTimeSeriesForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SupervisedTimeSeriesForest', model_string, SupervisedTimeSeriesForest_classification_hyperparams, imports,model_type)

class SupervisedTimeSeriesForestTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'SupervisedTimeSeriesForest()'
        imports = '''from sktime.classification.interval_based import SupervisedTimeSeriesForest\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SupervisedTimeSeriesForest', model_string, SupervisedTimeSeriesForest_classification_hyperparams, imports,model_type)