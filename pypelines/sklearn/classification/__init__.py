from .decision_tree_classification import DecisionTreeClassification, DecisionTreeClassificationComparison
from .logistic_regression import LogisticRegression, LogisticRegressionComparison
from .random_forest_classification import RandomForestClassification, RandomForestClassificationComparison
from .svc_classification import SVCClassification,SVCClassificationComparison
from .xgboost_classification import XGBoostClassification, XGBoostClassificationComparison
from .mlp_classification import MLPClassification, MLPClassificationComparison
from .ridge_classification import RidgeClassification,RidgeClassificationComparison


models_classification = {
    'Decision Tree': DecisionTreeClassification,
    'Logistic Regression': LogisticRegression,
    'Random Forest': RandomForestClassification,
    'SVC': SVCClassification,
    'XGBoost': XGBoostClassification,
    'MLP': MLPClassification,
    'Ridge Classifier': RidgeClassification
}

model_comparison_classification = {
    'Decision Tree': DecisionTreeClassificationComparison,
    'Logistic Regression': LogisticRegressionComparison,
    'Random Forest': RandomForestClassificationComparison,
    'SVC': SVCClassificationComparison,
    'XGBoost': XGBoostClassificationComparison,
    'MLP': MLPClassificationComparison,
    'Ridge Regression': RidgeClassificationComparison

}

__all__ = [
    #'DecisionTree',
    'LogisticRegression',
    'RandomForest',
    'SVC',
    #'XGBoost',
    'MLP'
]