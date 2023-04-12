from .decision_tree import DecisionTree, DecisionTreeComparison
from .logistic_regression import LogisticRegression, LogisticRegressionComparison
from .random_forest import RandomForest, RandomForestComparison
from .svc import SVC,SVCComparison
from .xgboost import XGBoost, XGBoostComparison
from .mlp import MLP, MLPComparison



models_classification = {
    #'Decision Tree': DecisionTree,
    'Logistic Regression': LogisticRegression,
    'Random Forest': RandomForest,
    'SVC': SVC,
    #'XGBoost': XGBoost,
    'MLP': MLP
}

model_comparison_classification = {
    #'Decision Tree': DecisionTreeComparison,
    'Logistic Regression': LogisticRegressionComparison,
    'Random Forest': RandomForestComparison,
    'SVC': SVCComparison,
    #'XGBoost': XGBoostComparison,
    'MLP': MLPComparison
}

__all__ = [
    #'DecisionTree',
    'LogisticRegression',
    'RandomForest',
    'SVC',
    #'XGBoost',
    'MLP'
]