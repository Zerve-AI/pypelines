from ..model_base import SklearnModelBase, SklearnModelComparisonBase


bernoulli_nb_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0, 'max': 1, 'step': 0.1},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_prior', 'selected': ['True'], 'values': ['True','False']},
        {'checked': True, 'name': 'force_alpha', 'selected': ['True'], 'values': ['True','False']},
    ]
}


class BernoulliNBClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'BernoulliNB()'
        imports = '''from naive_bayes import BernoulliNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('bernoulli_nb_classifier', model_string, bernoulli_nb_classification_hyperparams, imports,model_type)

class BernoulliNBClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'BernoulliNB()'
        imports = '''from naive_bayes import BernoulliNB\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('bernoulli_nb_classifier', model_string, bernoulli_nb_classification_hyperparams, imports,model_type)