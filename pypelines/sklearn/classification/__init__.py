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
from .extra_trees_classification import ExtraTreesClassification, ExtraTreesClassificationComparison
from .passive_aggressive_classification import PassiveAggressiveClassification,PassiveAggressiveClassificationComparison
from .lda_classification import LDAClassification, LDAClassificationComparison
from .qda_classification import QDAClassification, QDAClassificationComparison
from .nusvc_classification import NuSVCClassification, NuSVCClassificationComparison
from .guassian_nb_classification import GaussianNBClassification, GaussianNBClassificationComparison
from .multinomial_nb_classification import MultinomialNBClassification, MultinomialNBClassificationComparison
from .complement_nb_classification import ComplementNBClassification, ComplementNBClassificationComparison
from .bernoulii_nb_classification import BernoulliNBClassification, BernoulliNBClassificationComparison
from .categorical_nb_classification import CategoricalNBClassification, CategoricalNBClassificationComparison


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
    'ExtraTrees Classifier': ExtraTreesClassification,
    'PassiveAggressive Classifier': PassiveAggressiveClassification,
    'LDA Classifier': LDAClassification,
    'QDA Classifier': QDAClassification,
    'NuSVC Classifier': NuSVCClassification,
    'GaussianNB Classifier': GaussianNBClassification,
    'MultinomialNB Classifier': MultinomialNBClassification,
    'ComplementNB Classifier': ComplementNBClassification,
    'BernoulliNB Classifier': BernoulliNBClassification,
    'CategoricalNB Classifier': CategoricalNBClassification
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
    'ExtraTrees Classifier': ExtraTreesClassificationComparison,
    'PassiveAggressive Classifier': PassiveAggressiveClassificationComparison,
    'LDA Classifier': LDAClassificationComparison,
    'QDA Classifier': QDAClassificationComparison,
    'NuSVC Classifier': NuSVCClassificationComparison,
    'GaussianNB Classifier': GaussianNBClassificationComparison,
    'MultinomialNB Classifier': MultinomialNBClassificationComparison,
    'ComplementNB Classifier': ComplementNBClassificationComparison,
    'BernoulliNB Classifier': BernoulliNBClassificationComparison,
    'CategoricalNB Classifier': CategoricalNBClassificationComparison
}
