from ..model_base import SklearnModelBase, SklearnModelComparisonBase

qda_classification_hyperparams = {
    'numerical': [
    ],
    'categorical': [
        {'search': False, 'name': 'store_covariance', 'selected': [True], 'values': [True,False]},
    ]
}


class QDAClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'QuadraticDiscriminantAnalysis()'
        imports = '''from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('qda_classifier', model_string, qda_classification_hyperparams, imports,model_type)

class QDAClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'QuadraticDiscriminantAnalysis()'
        imports = '''from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('qda_classifier', model_string, qda_classification_hyperparams, imports,model_type)