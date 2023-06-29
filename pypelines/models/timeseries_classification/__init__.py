from .cnn_ts_classification import CNNTSClassifier, CNNTSClassifierComparison
from .lstmfcn_ts_classification import LSTMFCNTSClassifier, LSTMFCNTSClassifierComparison

models_ts_classification = {
    'CNN TS_Classifier': CNNTSClassifier,
    'LSTMFCN TS_Classifier': LSTMFCNTSClassifier
}

models_comparison_ts_classification = {
    'CNN TS_Classifier': CNNTSClassifierComparison,
    'LSTMFCN TS_Classifier': LSTMFCNTSClassifierComparison
}

models_ts_classification_default = {
    'CNN TS_Classifier': CNNTSClassifier,
    'LSTMFCN TS_Classifier': LSTMFCNTSClassifier
}

models_comparison_ts_classification_default = {
    'CNN TS_Classifier': CNNTSClassifierComparison,
    'LSTMFCN TS_Classifier': LSTMFCNTSClassifierComparison
}