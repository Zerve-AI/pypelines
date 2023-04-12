from ..model_base import SklearnModelBase,SklearnModelComparisonBase

logisitic_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'C', 'min': 0.1, 'max': 1, 'step': 0.1},
    ],
    'categorical': [
        {'checked': True, 'name': 'penalty', 'selected': ['l2'], 'values': ['l2', 'elasticnet', 'none']}
    ]
}


class LogisticRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'LogisticRegression()'
        imports = '''from sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('log_reg', model_string, logisitic_regression_hyperparams, imports,model_type)

class LogisticRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'LogisticRegression()'
        imports = '''from sklearn.linear_model import LogisticRegression\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('log_reg', model_string, logisitic_regression_hyperparams, imports,model_type)