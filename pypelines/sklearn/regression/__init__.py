from .elastic_net import ElasticNet,ElasticNetComparison
from .linear_regression import LinearRegression,LinearRegressionComparison
from .lasso import Lasso,LassoComparison

models_regression = {
    'Elastic Net': ElasticNet,
    'Linear Regression': LinearRegression,
    'Lasso': Lasso
}

model_comparison_regression = {
    'Elastic Net': ElasticNetComparison,
    'Linear Regression': LinearRegressionComparison,
    'Lasso': LassoComparison
}
