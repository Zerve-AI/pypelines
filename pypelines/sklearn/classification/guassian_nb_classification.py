from ..model_base import SklearnModelBase, SklearnModelComparisonBase


gaussian_nb_classification_hyperparams = {
    'numerical': [
    ],
    'categorical': [
    ]
}


class GaussianNBClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'GaussianNB()'
        imports = '''from naive_bayes import GaussianNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gaussian_nb_classifier', model_string, gaussian_nb_classification_hyperparams, imports,model_type)

class GaussianNBClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'GaussianNB()'
        imports = '''from naive_bayes import GaussianNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('gaussian_nb_classifier', model_string, gaussian_nb_classification_hyperparams, imports,model_type)