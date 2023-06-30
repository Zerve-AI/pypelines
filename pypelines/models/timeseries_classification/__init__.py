from .cnn import CNNTSClassifier, CNNTSClassifierComparison
from .lstmfcn import LSTMFCNTSClassifier, LSTMFCNTSClassifierComparison
from .fcn import FCNTSClassifier, FCNTSClassifierComparison
from .inceptiontime import InceptionTimeClassifier, InceptionTimeClassifierComparison
from .mlp import MLPTSClassifier, MLPTSClassifierComparison


models_ts_classification = {
    'CNN': CNNTSClassifier,
    'LSTMFCN': LSTMFCNTSClassifier,
    'FCN': FCNTSClassifier,
    'INCEPTIONTIME': InceptionTimeClassifier,
    'MLP': MLPTSClassifier
}

models_comparison_ts_classification = {
    'CNN': CNNTSClassifierComparison,
    'LSTMFCN': LSTMFCNTSClassifierComparison,
    'FCN': FCNTSClassifierComparison,
    'INCEPTIONTIME': InceptionTimeClassifierComparison,
    'MLP': MLPTSClassifierComparison
}

models_ts_classification_default = {
    'CNN': CNNTSClassifier,
    'LSTMFCN': LSTMFCNTSClassifier,
    'FCN': FCNTSClassifier,
    'INCEPTIONTIME': InceptionTimeClassifier,
    'MLP': MLPTSClassifier
}


models_comparison_ts_classification_default = {
    'CNN': CNNTSClassifierComparison,
    'LSTMFCN': LSTMFCNTSClassifierComparison,
    'FCN': FCNTSClassifierComparison,
    'INCEPTIONTIME': InceptionTimeClassifierComparison,
    'MLP': MLPTSClassifierComparison
}