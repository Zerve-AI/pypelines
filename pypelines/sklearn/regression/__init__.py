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
from .extra_tree_regression import ExtraTreeRegression, ExtraTreeRegressionComparison
from .gpr_regression import GPRRegression, GPRRegressionComparison
from .bayesian_ard_regression import ARDRegression, ARDRegressionComparison
from .bayesianridge_regression import BayesianRidgeRegression, BayesianRidgeRegressionComparison
from .quantile_regression import QuantileRegression, QuantileRegressionComparison
from .huber_regression import HuberRegression, HuberRegressionComparison
from .theilsen_regression import TheilSenRegression, TheilSenRegressionComparison
from .passiveaggressive_regression import PassiveAggressiveRegression, PassiveAggressiveRegressionComparison
from .gamma_regression import GammaRegression, GammaRegressionComparison
from .tweedie_regression import TweedieRegression, TweedieRegressionComparison
from .omp_regression import OMPRegression, OMPRegressionComparison
from .lassolars_regression import LassoLarsRegression, LassoLarsRegressionComparison
from .ransac_regression import RANSACRegression, RANSACRegressionComparison


models_regression = {
    'Elastic Net Regression': ElasticNetRegression,
    'Linear Regression': LinearRegression,
    'Lasso Regression': LassoRegression,
    'Ridge Regression': RidgeRegression,
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
    'Bayesian Ridge Regression': BayesianRidgeRegression,
    'Quantile Regression': QuantileRegression,
    'Huber Regression': HuberRegression,
    'TheilSen Regression': TheilSenRegression,
    'Passive Aggressive Regression': PassiveAggressiveRegression,
    'Gamma Regression': GammaRegression,
    'Tweedie Regression': TweedieRegression,
    'OMP Regression': OMPRegression,
    'LassoLars Regression': LassoLarsRegression,
    'RANSAC Regression': RANSACRegression
}

model_comparison_regression = {
    'Elastic Net Regression': ElasticNetRegressionComparison,
    'Linear Regression': LinearRegressionComparison,
    'Lasso Regression': LassoRegressionComparison,
    'Ridge Regression': RidgeRegressionComparison,
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
    'Bayesian Ridge Regression': BayesianRidgeRegressionComparison,
    'Quantile Regression': QuantileRegressionComparison,
    'Huber Regression': HuberRegressionComparison,
    'TheilSen Regression': TheilSenRegressionComparison,
    'Passive Aggressive Regression': PassiveAggressiveRegressionComparison,
    'Gamma Regression': GammaRegressionComparison,
    'Tweedie Regression': TweedieRegressionComparison,
    'OMP Regression': OMPRegressionComparison,
    'LassoLars Regression': LassoLarsRegressionComparison,
    'RANSAC Regression': RANSACRegressionComparison
}
