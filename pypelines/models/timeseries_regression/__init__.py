from .cnn_regression import CNNTSRegression, CNNTSRegressionComparison
from .knn import KNNTSRegression, KNNTSRegressionComparison
from .tapnet import TapNetTSRegression, TapNetTSRegressionComparison
from .dummy import DUMMYTSRegression, DUMMYTSRegressionComparison


models_ts_regression = {
    'CNN': CNNTSRegression,
    'KNN': KNNTSRegression,
    'TAPNET': TapNetTSRegression,
    'DUMMY': DUMMYTSRegression
}

models_comparison_ts_regression = {
    'CNN': CNNTSRegressionComparison,
    'KNN': KNNTSRegressionComparison,
    'TAPNET': TapNetTSRegressionComparison,
    'DUMMY': DUMMYTSRegressionComparison
}

models_ts_regression_default = {
    'CNN': CNNTSRegression,
    'KNN': KNNTSRegression,
    'TAPNET': TapNetTSRegression,
    'DUMMY': DUMMYTSRegression
}


models_comparison_ts_regression_default = {
    'CNN': CNNTSRegressionComparison,
    'KNN': KNNTSRegressionComparison,
    'TAPNET': TapNetTSRegressionComparison,
    'DUMMY': DUMMYTSRegressionComparison
}