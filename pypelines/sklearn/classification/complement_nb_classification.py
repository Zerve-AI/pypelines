from ..model_base import SklearnModelBase, SklearnModelComparisonBase


complement_nb_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 1, 'step': 0.1},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_prior', 'selected': [True], 'values': [True,False]},
        {'search': False, 'name': 'force_alpha', 'selected': [True], 'values': [True,False]},
    ]
}


class ComplementNBClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'ComplementNB()'
        imports = '''from sklearn.naive_bayes import ComplementNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('complement_nb_classifier', model_string, complement_nb_classification_hyperparams, imports,model_type)

class ComplementNBClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ComplementNB()'
        imports = '''from sklearn.naive_bayes import ComplementNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('complement_nb_classifier', model_string, complement_nb_classification_hyperparams, imports,model_type)