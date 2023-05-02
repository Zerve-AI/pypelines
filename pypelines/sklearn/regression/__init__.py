from .elastic_net_regression import ElasticNetRegression,ElasticNetRegressionComparison
from .linear_regression import LinearRegression,LinearRegressionComparison
from .lasso_regression import LassoRegression,LassoRegressionComparison
from .ridge_regression import RidgeRegression,RidgeRegressionComparison
from .ridge_regression import RidgeRegression,RidgeRegressionComparison
from .sgd_regression import SGDRegression, SGDRegressionComparison
from .histgbt_regression import HistGBTRegression, HistGBTRegressionComparison
from .random_forest_regression import RandomForestRegression, RandomForestRegressionComparison
from .adaboost_regression import AdaBoostRegression, AdaBoostRegressionComparison
from .poisson_regression import PoissonRegression, PoissonRegressionComparison
from .decision_tree import DecisionTreeRegression, DecisionTreeRegressionComparison
from .gbt_regression import GBTRegression, GBTRegressionComparison
from.extra_tree_regression import ExtraTreeRegression, ExtraTreeRegressionComparison
from .gpr_regression import GPRRegression, GPRRegressionComparison
from .bayesian_ard_regression import ARDRegression, ARDRegressionComparison
from .bayesianridge_regression import BayesianRidgeRegression, BayesianRidgeRegressionComparison

models_regression = {
    'Elastic Net': ElasticNetRegression,
    'Linear Regression': LinearRegression,
    'Lasso': LassoRegression,
    'Ridge': RidgeRegression,
    'SGD Regressor Regression': SGDRegression,
    'Histogram Gradient Boost Regression': HistGBTRegression,
    'Random Forest Regression': RandomForestRegression,
    'AdaBoost Regression': AdaBoostRegression,
    'Poisson Regression': PoissonRegression,
    'Decision Tree Regression': DecisionTreeRegression,
    'GBT Regression': GBTRegression,
    'ExtraTree Regression': ExtraTreeRegression,
    'GPR Regression': GPRRegression,
    'Bayesian ARD Regression': ARDRegression,
    'Bayesian Ridge Regression': BayesianRidgeRegression
}

model_comparison_regression = {
    'Elastic Net': ElasticNetRegressionComparison,
    'Linear Regression': LinearRegressionComparison,
    'Lasso': LassoRegressionComparison,
    'Ridge': RidgeRegressionComparison,
    'SGD Regressor Regression': SGDRegressionComparison,
    'Histogram Gradient Boost Regression': HistGBTRegressionComparison,
    'Random Forest Regression': RandomForestRegressionComparison,
    'AdaBoost Regression': AdaBoostRegressionComparison,
    'Poisson Regression': PoissonRegressionComparison,
    'Decision Tree Regression': DecisionTreeRegressionComparison,
    'GBT Regression': GBTRegressionComparison,
    'ExtraTree Regression': ExtraTreeRegressionComparison,
    'GPR Regression': GPRRegressionComparison,
    'Bayesian ARD Regression': ARDRegressionComparison,
    'Bayesian Ridge Regression': BayesianRidgeRegressionComparison
}
