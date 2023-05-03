from ..model_base import SklearnModelBase, SklearnModelComparisonBase

gaussian_process_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'max_iter_predict', 'min': 100, 'max': 10000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'warm_start', 'selected': ['True'], 'values': ['True', 'False']},
    ]
}


class GaussianProcessClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'GaussianProcessClassifier()'
        imports = '''from sklearn.gaussian_process import GaussianProcessClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gaussian_process_classifier', model_string, gaussian_process_classification_hyperparams, imports,model_type)

class GaussianProcessClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GaussianProcessClassifier()'
        imports = '''from sklearn.gaussian_process import GaussianProcessClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gaussian_process_classifier', model_string, gaussian_process_classification_hyperparams, imports,model_type)