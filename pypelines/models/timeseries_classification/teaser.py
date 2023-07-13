from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

TEASER_classification_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'estimator', 'selected': [None], 'values': ['sklearn classifier',None]}
    ]
}


class TEASERTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'TEASER()'
        imports = '''from sktime.classification.early_classification import TEASER\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TEASER', model_string, TEASER_classification_hyperparams, imports,model_type)

class TEASERTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'TEASER()'
        imports = '''from sktime.classification.early_classification import TEASER\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('TEASER', model_string, TEASER_classification_hyperparams, imports,model_type)