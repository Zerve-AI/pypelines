from ..model_base import SklearnModelBase, SklearnModelComparisonBase


xgboost_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'learning_rate', 'min': 0.1, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'n_estimators', 'min': 100, 'max': 500, 'step': 50},
        {'checked': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'checked': True, 'name': 'gamma', 'min': 0.0, 'max': 0.5, 'step': 0.1},
        {'checked': True, 'name': 'subsample', 'min': 0.1, 'max': 1.0, 'step': 0.25},
        {'checked': True, 'name': 'colsample_bytree', 'min': 0.5, 'max': 1.0, 'step': 0.1},
        {'checked': True, 'name': 'reg_alpha', 'min': 0.0, 'max': 1.0, 'step': 0.1},
        {'checked': True, 'name': 'reg_lambda', 'min': 0.0, 'max': 1.0, 'step': 0.1},
    ],
    'categorical': [
        {'checked': True, 'name': 'booster', 'selected': ['gbtree'], 'values':  ['gbtree', 'gblinear', 'dart']},
        {'checked': True, 'name': 'eval_metric', 'selected': ['rmse'], 'values': ['rmse', 'mae', 'logloss', 'error', 'merror', 'mlogloss', 'auc']},
        {'checked': True, 'name': 'tree_method', 'selected': ['auto'], 'values': ['auto', 'exact', 'approx', 'hist', 'gpu_hist']},
        {'checked': True, 'name': 'grow_policy', 'selected': ['depthwise'], 'values': ['depthwise', 'lossguide']},
    ]
}


class XGBoostClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'XGBClassifier()'
        imports = '''from xgboost import XGBClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('xgboost_classifier', model_string, xgboost_classification_hyperparams, imports,model_type)

class XGBoostClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'XGBClassifier()'
        imports = '''from xgboost import XGBClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('xgboost_classifier', model_string, xgboost_classification_hyperparams, imports,model_type)