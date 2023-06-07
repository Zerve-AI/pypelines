from ..model_base import SklearnModelBase, SklearnModelComparisonBase


xgboost_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'learning_rate', 'min': 0.1, 'max': 1, 'step': 0.25},
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 500, 'step': 100},
        {'search': True, 'name': 'max_depth', 'min': 2, 'max': 10, 'step': 2},
        {'search': True, 'name': 'gamma', 'min': 0.0, 'max': 0.5, 'step': 0.25},
        {'search': True, 'name': 'subsample', 'min': 0.1, 'max': 1.0, 'step': 0.25},
        {'search': True, 'name': 'colsample_bytree', 'min': 0.5, 'max': 1.0, 'step': 0.25}
    ],
    'categorical': [
        {'search': False, 'name': 'booster', 'selected': ['gbtree'], 'values':  ['gbtree', 'gblinear', 'dart']},
        {'search': False, 'name': 'eval_metric', 'selected': ['rmse'], 'values': ['rmse', 'mae', 'logloss', 'error', 'merror', 'mlogloss', 'auc']},
        {'search': False, 'name': 'tree_method', 'selected': ['auto'], 'values': ['auto', 'exact', 'approx', 'hist', 'gpu_hist']},
        {'search': False, 'name': 'grow_policy', 'selected': ['depthwise'], 'values': ['depthwise', 'lossguide']},
    ]
}


class XGBoostClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'XGBClassifier()'
        imports = '''from xgboost import XGBClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('xgboost_classifier', model_string, xgboost_classification_hyperparams, imports,model_type)

class XGBoostClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'XGBClassifier()'
        imports = '''from xgboost import XGBClassifier\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('xgboost_classifier', model_string, xgboost_classification_hyperparams, imports,model_type)