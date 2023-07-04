from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ProbabilityTEC_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'probability_threshold', 'min': 0.5, 'max': 1, 'step': 0.05}
    ]
}


class ProbabilityTECTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ProbabilityThresholdEarlyClassifier()'
        imports = '''from sktime.classification.early_classification import ProbabilityThresholdEarlyClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProbabilityThresholdEarlyClassifier', model_string, ProbabilityTEC_classification_hyperparams, imports,model_type)

class ProbabilityTECTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ProbabilityThresholdEarlyClassifier()'
        imports = '''from sktime.classification.early_classification import ProbabilityThresholdEarlyClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ProbabilityThresholdEarlyClassifier', model_string, ProbabilityTEC_classification_hyperparams, imports,model_type)