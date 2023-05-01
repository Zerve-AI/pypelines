from .decision_tree_classification import DecisionTreeClassification, DecisionTreeClassificationComparison
from .logistic_regression import LogisticRegression, LogisticRegressionComparison
from .random_forest_classification import RandomForestClassification, RandomForestClassificationComparison
from .svc_classification import SVCClassification,SVCClassificationComparison
from .xgboost_classification import XGBoostClassification, XGBoostClassificationComparison
from .mlp_classification import MLPClassification, MLPClassificationComparison
from .ridge_classification import RidgeClassification,RidgeClassificationComparison
from .histgbt_classification import HistGBTClassification,HistGBTClassificationComparison
from .perceptron_classification import PerceptronClassification, PerceptronClassificationComparison
from .sgd_classification import SGDClassification, SGDClassificationComparison
from .gbt_classification import GBTClassification, GBTClassificationComparison
from .adaboost_classification import ADABoostClassification, ADABoostClassificationComparison



models_classification = {
    'Decision Tree': DecisionTreeClassification,
    'Logistic Regression': LogisticRegression,
    'Random Forest': RandomForestClassification,
    'SVC': SVCClassification,
    'XGBoost': XGBoostClassification,
    'MLP': MLPClassification,
    'Ridge Classifier': RidgeClassification,
    'HistGBT Classifier': HistGBTClassification,
    'Perceptron Classifier':PerceptronClassification,
    'SGD Classifier': SGDClassification,
    'GBT Classifier': GBTClassification,
    'ADABoost Classifier': ADABoostClassification,
}

model_comparison_classification = {
    'Decision Tree': DecisionTreeClassificationComparison,
    'Logistic Regression': LogisticRegressionComparison,
    'Random Forest': RandomForestClassificationComparison,
    'SVC': SVCClassificationComparison,
    'XGBoost': XGBoostClassificationComparison,
    'MLP': MLPClassificationComparison,
    'Ridge Classifier': RidgeClassificationComparison,
    'HistGBT Classifier': HistGBTClassificationComparison,
    'Perceptron Classifier':PerceptronClassificationComparison,
    'SGD Classifier': SGDClassificationComparison,
    'GBT Classifier': GBTClassificationComparison,
    'ADABoost Classifier': ADABoostClassificationComparison,
}

__all__ = [
    #'DecisionTree',
    'LogisticRegression',
    'RandomForest',
    'SVC',
    #'XGBoost',
    'MLP'
]