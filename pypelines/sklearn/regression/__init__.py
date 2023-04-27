from .elastic_net_regression import ElasticNetRegression,ElasticNetRegressionComparison
from .linear_regression import LinearRegression,LinearRegressionComparison
from .lasso_regression import LassoRegression,LassoRegressionComparison
from .ridge_regression import RidgeRegression,RidgeRegressionComparison

models_regression = {
    'Elastic Net': ElasticNetRegression,
    'Linear Regression': LinearRegression,
    'Lasso': LassoRegression,
    'Ridge': RidgeRegression
}

model_comparison_regression = {
    'Elastic Net': ElasticNetRegressionComparison,
    'Linear Regression': LinearRegressionComparison,
    'Lasso': LassoRegressionComparison,
    'Ridge': RidgeRegressionComparison
}
