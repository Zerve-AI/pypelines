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
from .proximitystump import ProximityStumpTSClassifier, ProximityStumpTSClassifierComparison
from .proximitytree import ProximityTreeTSClassifier, ProximityTreeTSClassifierComparison
from .shapedtw import ShapeDTWTSClassifier, ShapeDTWSTSClassifierComparison
from .rotation_forest import RotationForestTSClassifier, RotationForestTSClassifierComparison
from .rocket_classifier import RocketTSClassifier, RocketTSClassifierComparison
from .arsenal import ArsenalTSClassifier, ArsenalTSClassifierComparison
from .timeseries_svc import TimeSeriesSVCTSClassifier, TimeSeriesSVCTSClassifierComparison
from .mrsqm import MrSQMTSClassifier, MrSQMTSClassifierComparison
from .continuous_interval_tree import ContinuousIntervalTreeTSClassifier, ContinuousIntervalTreeTSClassifierComparison
from .shapelet_transform_classifier import ShapeletTransformTSClassifier, ShapeletTransformTSClassifierComparison
from .timeseries_forest_classifier import TimeSeriesForestTSClassifier, TimeSeriesForestTSClassifierComparison
from .supervised_timeseries_forest import SupervisedTimeSeriesForestTSClassifier, SupervisedTimeSeriesForestTSClassifierComparison
from .drcif import DrCIFTSClassifier, DrCIFTSClassifierComparison
from .random_ise import RandomISETSClassifier, RandomISETSClassifierComparison
from .canonical_if import CanonicalIFTSClassifier, CanonicalIFTSClassifierComparison
from .hivecotev2 import HIVECOTEV2TSClassifier, HIVECOTEV2TSClassifierComparison
from .hivecotev1 import HIVECOTEV1TSClassifier, HIVECOTEV1TSClassifierComparison
from .tsfreshclassifier import TSFreshTSClassifier, TSFreshTSClassifierComparison
from .summaryclassifier import SummaryTSClassifier, SummaryTSClassifierComparison
from .signatureclassifier import SignatureTSClassifier, SignatureTSClassifierComparison
from .teaser import TEASERTSClassifier, TEASERTSClassifierComparison
from .probability_tec import ProbabilityTECTSClassifier, ProbabilityTECTSClassifierComparison
from .catch22classifier import Catch22TSClassifier, Catch22TSClassifierComparison
from .Fresh_prince import FreshPRINCETSClassifier, FreshPRINCETSClassifierComparison
from .matrix_pc import MatrixPCTSClassifier, MatrixPCTSClassifierComparison
from .random_ic import RandomICTSClassifier, RandomICTSClassifierComparison



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
    'ProximityStump': ProximityStumpTSClassifier,
    'ProximityTree':ProximityTreeTSClassifier,
    'ShapeDTW': ShapeDTWTSClassifier,
    #'RotationForest': RotationForestTSClassifier,
    'RocketClassifer': RocketTSClassifier,
    'Arsenal': ArsenalTSClassifier,
    #'TimeSeriesSVC': TimeSeriesSVCTSClassifier,
    #'MrSQM': MrSQMTSClassifier,
    #'ContinuousIntervalTree': ContinuousIntervalTreeTSClassifier,
    'ShapeletTransformClassifier': ShapeletTransformTSClassifier,
    'TimeSeriesForestClassifier': TimeSeriesForestTSClassifier,
    'SupervisedTimeSeriesForestClassifier': SupervisedTimeSeriesForestTSClassifier,
    'DrCIF': DrCIFTSClassifier,
    'RandomIntervalSpectralEnsemble': RandomISETSClassifier,
    'CanonicalIntervalForest': CanonicalIFTSClassifier,
    'HIVECOTEV2': HIVECOTEV2TSClassifier,
    'HIVECOTEV1': HIVECOTEV1TSClassifier,
    'TSFreshClassifier': TSFreshTSClassifier,
    'SummaryClassifier': SummaryTSClassifier,
    'SignatureClassifier': SignatureTSClassifier,
    #'TEASER': TEASERTSClassifier,
    #'ProbabilityThresholdEarlyClassifier': ProbabilityTECTSClassifier,
    'Catch22Classifier': Catch22TSClassifier,
    'FreshPRINCE': FreshPRINCETSClassifier,
    'MatrixProfileClassifier': MatrixPCTSClassifier,
    'RandomIntervalClassifier': RandomICTSClassifier
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
    'ProximityStump': ProximityStumpTSClassifierComparison,
    'ProximityTree':ProximityTreeTSClassifierComparison,
    'ShapeDTW': ShapeDTWSTSClassifierComparison, 
    #'RotationForest': RotationForestTSClassifierComparison,
    'RocketClassifer': RocketTSClassifierComparison,
    'Arsenal': ArsenalTSClassifierComparison,
    #'TimeSeriesSVC': TimeSeriesSVCTSClassifierComparison,
    #'MrSQM': MrSQMTSClassifierComparison,
    #'ContinuousIntervalTree': ContinuousIntervalTreeTSClassifierComparison,
    'ShapeletTransformClassifier': ShapeletTransformTSClassifierComparison,
    'TimeSeriesForestClassifier': TimeSeriesForestTSClassifierComparison,
    'SupervisedTimeSeriesForestClassifier': SupervisedTimeSeriesForestTSClassifierComparison,
    'DrCIF': DrCIFTSClassifierComparison,
    'RandomIntervalSpectralEnsemble': RandomISETSClassifierComparison,
    'CanonicalIntervalForest': CanonicalIFTSClassifierComparison,
    'HIVECOTEV2': HIVECOTEV2TSClassifierComparison,
    'HIVECOTEV1': HIVECOTEV1TSClassifierComparison,
    'TSFreshClassifier': TSFreshTSClassifierComparison,
    'SummaryClassifier': SummaryTSClassifierComparison,
    'SignatureClassifier': SignatureTSClassifierComparison,
    #'TEASER': TEASERTSClassifierComparison,
    #'ProbabilityThresholdEarlyClassifier': ProbabilityTECTSClassifierComparison,
    'Catch22Classifier': Catch22TSClassifierComparison,
    'FreshPRINCE': FreshPRINCETSClassifierComparison,
    'MatrixProfileClassifier': MatrixPCTSClassifierComparison,
    'RandomIntervalClassifier': RandomICTSClassifierComparison
    
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
    'ProximityStump': ProximityStumpTSClassifier,
    'ProximityTree':ProximityTreeTSClassifier,
    'ShapeDTW': ShapeDTWTSClassifier,
    #'RotationForest': RotationForestTSClassifier,
    'RocketClassifer': RocketTSClassifier,
    'Arsenal': ArsenalTSClassifier,
    #'TimeSeriesSVC': TimeSeriesSVCTSClassifier,
    #'MrSQM': MrSQMTSClassifier,
    #'ContinuousIntervalTree': ContinuousIntervalTreeTSClassifier,
    'ShapeletTransformClassifier': ShapeletTransformTSClassifier,
    'TimeSeriesForestClassifier': TimeSeriesForestTSClassifier,
    'SupervisedTimeSeriesForestClassifier': SupervisedTimeSeriesForestTSClassifier,
    'DrCIF': DrCIFTSClassifier,
    'RandomIntervalSpectralEnsemble': RandomISETSClassifier,
    'CanonicalIntervalForest': CanonicalIFTSClassifier,
    'HIVECOTEV2': HIVECOTEV2TSClassifier,
    'HIVECOTEV1': HIVECOTEV1TSClassifier,
    'TSFreshClassifier': TSFreshTSClassifier,
    'SummaryClassifier': SummaryTSClassifier,
    'SignatureClassifier': SignatureTSClassifier,
    #'TEASER': TEASERTSClassifier,
    #'ProbabilityThresholdEarlyClassifier': ProbabilityTECTSClassifier,
    'Catch22Classifier': Catch22TSClassifier,
    'FreshPRINCE': FreshPRINCETSClassifier,
    'MatrixProfileClassifier': MatrixPCTSClassifier,
    'RandomIntervalClassifier': RandomICTSClassifier
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
    'ProximityStump': ProximityStumpTSClassifierComparison,
    'ProximityTree':ProximityTreeTSClassifierComparison,
    'ShapeDTW': ShapeDTWSTSClassifierComparison,
    #'RotationForest': RotationForestTSClassifierComparison,
    'RocketClassifer': RocketTSClassifierComparison,
    'Arsenal': ArsenalTSClassifierComparison,
    #'TimeSeriesSVC': TimeSeriesSVCTSClassifierComparison,
    #'MrSQM': MrSQMTSClassifierComparison,
    #'ContinuousIntervalTree': ContinuousIntervalTreeTSClassifierComparison,
    'ShapeletTransformClassifier': ShapeletTransformTSClassifierComparison,
    'TimeSeriesForestClassifier': TimeSeriesForestTSClassifierComparison,
    'SupervisedTimeSeriesForestClassifier': SupervisedTimeSeriesForestTSClassifierComparison,
    'DrCIF': DrCIFTSClassifierComparison,
    'RandomIntervalSpectralEnsemble': RandomISETSClassifierComparison,
    'CanonicalIntervalForest': CanonicalIFTSClassifierComparison,
    'HIVECOTEV2': HIVECOTEV2TSClassifierComparison,
    'HIVECOTEV1': HIVECOTEV1TSClassifierComparison,
    'TSFreshClassifier': TSFreshTSClassifierComparison,
    'SummaryClassifier': SummaryTSClassifierComparison,
    'SignatureClassifier': SignatureTSClassifierComparison,
    #'TEASER': TEASERTSClassifierComparison,
    #'ProbabilityThresholdEarlyClassifier': ProbabilityTECTSClassifierComparison,
    'Catch22Classifier': Catch22TSClassifierComparison,
    'FreshPRINCE': FreshPRINCETSClassifierComparison,
    'MatrixProfileClassifier': MatrixPCTSClassifierComparison,
    'RandomIntervalClassifier': RandomICTSClassifierComparison
}