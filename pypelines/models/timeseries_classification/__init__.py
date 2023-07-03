from .cnn import CNNTSClassifier, CNNTSClassifierComparison
from .lstmfcn import LSTMFCNTSClassifier, LSTMFCNTSClassifierComparison
from .fcn import FCNTSClassifier, FCNTSClassifierComparison
from .inceptiontime import InceptionTimeClassifier, InceptionTimeClassifierComparison
from .mlp import MLPTSClassifier, MLPTSClassifierComparison
from .tapnet import TapNetTSClassifier, TapNetTSClassifierComparison
from .bossensemble import BOSSEnsembleTSClassifier, BOSSEnsembleTSClassifierComparison
from .contractableboss import ContractableBOSSTSClassifier, ContractableBOSSTSClassifierComparison
from .elasticensemble import ElasticEnsembleTSClassifier, ElasticEnsembleTSClassifierComparison
from .knn import KNNTSClassifier, KNNTSClassifierComparison
from .proximityforest import ProximityForestTSClassifier, ProximityForestTSClassifierComparison




models_ts_classification = {
    'CNN': CNNTSClassifier,
    'LSTMFCN': LSTMFCNTSClassifier,
    'FCN': FCNTSClassifier,
    'INCEPTIONTIME': InceptionTimeClassifier,
    'MLP': MLPTSClassifier,
    'TAPNET': TapNetTSClassifier,
    'BOSSENSEMBLE': BOSSEnsembleTSClassifier,
    'CONTRACTABLEBOSS': ContractableBOSSTSClassifier,
    'ElasticEnsemble':ElasticEnsembleTSClassifier,
    'KNN': KNNTSClassifier,
    'ProximityForest': ProximityForestTSClassifier,
}

models_comparison_ts_classification = {
    'CNN': CNNTSClassifierComparison,
    'LSTMFCN': LSTMFCNTSClassifierComparison,
    'FCN': FCNTSClassifierComparison,
    'INCEPTIONTIME': InceptionTimeClassifierComparison,
    'MLP': MLPTSClassifierComparison,
    'TAPNET': TapNetTSClassifierComparison,
    'BOSSENSEMBLE': BOSSEnsembleTSClassifierComparison,
    'CONTRACTABLEBOSS': ContractableBOSSTSClassifierComparison,
    'ElasticEnsemble':ElasticEnsembleTSClassifierComparison,
    'KNN': KNNTSClassifierComparison,
    'ProximityForest': ProximityForestTSClassifierComparison,
}

models_ts_classification_default = {
    'CNN': CNNTSClassifier,
    'LSTMFCN': LSTMFCNTSClassifier,
    'FCN': FCNTSClassifier,
    'INCEPTIONTIME': InceptionTimeClassifier,
    'MLP': MLPTSClassifier,
    'TAPNET': TapNetTSClassifier,
    'BOSSENSEMBLE': BOSSEnsembleTSClassifier,
    'CONTRACTABLEBOSS': ContractableBOSSTSClassifier,
    'ElasticEnsemble':ElasticEnsembleTSClassifier,
    'KNN': KNNTSClassifier,
    'ProximityForest': ProximityForestTSClassifier,
}


models_comparison_ts_classification_default = {
    'CNN': CNNTSClassifierComparison,
    'LSTMFCN': LSTMFCNTSClassifierComparison,
    'FCN': FCNTSClassifierComparison,
    'INCEPTIONTIME': InceptionTimeClassifierComparison,
    'MLP': MLPTSClassifierComparison,
    'TAPNET': TapNetTSClassifierComparison,
    'BOSSENSEMBLE': BOSSEnsembleTSClassifierComparison,
    'CONTRACTABLEBOSS': ContractableBOSSTSClassifierComparison,
    'ElasticEnsemble':ElasticEnsembleTSClassifierComparison,
    'KNN': KNNTSClassifierComparison,
    'ProximityForest': ProximityForestTSClassifierComparison,
}