from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

MatrixPC_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'subsequence_length', 'min': 2, 'max': 10, 'step': 2}
    ]
}


class MatrixPCTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'MatrixProfileClassifier()'
        imports = '''from sktime.classification.feature_based import MatrixProfileClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MatrixProfileClassifier', model_string, MatrixPC_TS_classification_hyperparams, imports,model_type)

class MatrixPCTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'MatrixProfileClassifier()'
        imports = '''from sktime.classification.feature_based import MatrixProfileClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('MatrixProfileClassifier', model_string, MatrixPC_TS_classification_hyperparams, imports,model_type)