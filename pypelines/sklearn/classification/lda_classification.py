from ..model_base import SklearnModelBase, SklearnModelComparisonBase

lda_classification_hyperparams = {
    'categorical': [
        {'checked': True, 'name': 'solver', 'selected': ['svd'], 'values': ['svd', 'lsqr', 'eigen']},
    ]
}


class LDAClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'LinearDiscriminantAnalysis()'
        imports = '''from sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('lda_classifier', model_string, lda_classification_hyperparams, imports,model_type)

class LDAClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'LinearDiscriminantAnalysis()'
        imports = '''from sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('lda_classifier', model_string, lda_classification_hyperparams, imports,model_type)