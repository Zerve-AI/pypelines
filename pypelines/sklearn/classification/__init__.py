from .decision_tree_classification import DecisionTreeClassification, DecisionTreeClassificationComparison
from .logistic_regression import LogisticRegression, LogisticRegressionComparison
from .random_forest_classification import RandomForestClassification, RandomForestClassificationComparison
from .svc_classification import SVCClassification,SVCClassificationComparison
from .xgboost_classification import XGBoostClassification, XGBoostClassificationComparison
from .mlp_classification import MLPClassification, MLPClassificationComparison
from .ridge_classification import RidgeClassification,RidgeClassificationComparison
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
from .gaussian_process_classification import GaussianProcessClassification, GaussianProcessClassificationComparison


models_classification = {
    'Decision Tree Classifier': DecisionTreeClassification,
    'Logistic Regression': LogisticRegression,
    'Random Forest Classifier': RandomForestClassification,
    'SVC Classifier': SVCClassification,
    'XGBoost Classifier': XGBoostClassification,
    'MLP Classifier': MLPClassification,
    'Ridge Classifier': RidgeClassification, 
    'Perceptron Classifier':PerceptronClassification,
    'SGD Classifier': SGDClassification,
    'GBT Classifier': GBTClassification,
    'ADABoost Classifier': ADABoostClassification,
    'ExtraTrees Classifier': ExtraTreesClassification,
    'PassiveAggressive Classifier': PassiveAggressiveClassification,
    #'LDA Classifier': LDAClassification,
    #'QDA Classifier': QDAClassification,
    'NuSVC Classifier': NuSVCClassification,
    #'GaussianNB Classifier': GaussianNBClassification,
    'MultinomialNB Classifier': MultinomialNBClassification,
    'ComplementNB Classifier': ComplementNBClassification,
    'BernoulliNB Classifier': BernoulliNBClassification,
    #'CategoricalNB Classifier': CategoricalNBClassification,
    'Gaussian Process Classifier': GaussianProcessClassification
}

models_comparison_classification = {
    'Decision Tree Classifier': DecisionTreeClassificationComparison,
    'Logistic Regression': LogisticRegressionComparison,
    'Random Forest Classifier': RandomForestClassificationComparison,
    'SVC Classifier': SVCClassificationComparison,
    'XGBoost Classifier': XGBoostClassificationComparison,
    'MLP Classifier': MLPClassificationComparison,
    'Ridge Classifier': RidgeClassificationComparison,
    'Perceptron Classifier':PerceptronClassificationComparison,
    'SGD Classifier': SGDClassificationComparison,
    'GBT Classifier': GBTClassificationComparison,
    'ADABoost Classifier': ADABoostClassificationComparison,
    'ExtraTrees Classifier': ExtraTreesClassificationComparison,
    'PassiveAggressive Classifier': PassiveAggressiveClassificationComparison,
    #'LDA Classifier': LDAClassificationComparison,to_array()
    #'QDA Classifier': QDAClassificationComparison,to_array()
    'NuSVC Classifier': NuSVCClassificationComparison,
    #'GaussianNB Classifier': GaussianNBClassificationComparison,#to_array()
    'MultinomialNB Classifier': MultinomialNBClassificationComparison,
    'ComplementNB Classifier': ComplementNBClassificationComparison, 
    'BernoulliNB Classifier': BernoulliNBClassificationComparison,
    #'CategoricalNB Classifier': CategoricalNBClassificationComparison, #to_array()
    'Gaussian Process Classifier': GaussianProcessClassificationComparison
}


models_classification_default = {
    'Decision Tree Classifier': DecisionTreeClassification,
    'Logistic Regression': LogisticRegression,
    'Random Forest Classifier': RandomForestClassification,
    'XGBoost Classifier': XGBoostClassification,
    'GBT Classifier': GBTClassification
}

models_comparison_classification_default = {
    'Decision Tree Classifier': DecisionTreeClassificationComparison,
    'Logistic Regression': LogisticRegressionComparison,
    'Random Forest Classifier': RandomForestClassificationComparison,
    'XGBoost Classifier': XGBoostClassificationComparison,
    'GBT Classifier': GBTClassificationComparison,
}