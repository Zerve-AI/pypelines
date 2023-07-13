from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

Summary_classification_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'estimator', 'selected': [None], 'values': ['sklearn classifier',None]}
    ]
}


class SummaryTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'SummaryClassifier()'
        imports = '''from sktime.classification.feature_based import SummaryClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SummaryClassifier', model_string, Summary_classification_hyperparams, imports,model_type)

class SummaryTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'SummaryClassifier()'
        imports = '''from sktime.classification.feature_based import SummaryClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('SummaryClassifier', model_string, Summary_classification_hyperparams, imports,model_type)