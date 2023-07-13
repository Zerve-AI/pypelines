from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ElasticEnsemble_TS_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'proportion_of_param_options', 'min': 0.1, 'max': 1, 'step': 0.5},
        {'search': False, 'name': 'proportion_train_for_test', 'min': 0.1, 'max': 1, 'step': 0.5},
    ],
    'categorical': [
        {'search': True, 'name': 'distance_measures', 'selected': ['euclidean'], 'values': ['euclidean', 'dtw', 'wdtw',
                                                                                           'ddtw', 'dwdtw', 'lcss', 'erp', 'msm']},
    ]
}


class ElasticEnsembleTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ElasticEnsemble()'
        imports = '''from sktime.classification.distance_based import ElasticEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ElasticEnsemble', model_string, ElasticEnsemble_TS_classification_hyperparams, imports,model_type)

class ElasticEnsembleTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ElasticEnsemble()'
        imports = '''from sktime.classification.distance_based import ElasticEnsemble\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ElasticEnsemble', model_string, ElasticEnsemble_TS_classification_hyperparams, imports,model_type)