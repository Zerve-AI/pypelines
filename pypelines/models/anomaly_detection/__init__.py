from .abod import ABODAnomalyDetection, ABODAnomalyDetectionComparison
from .alad import ALADAnomalyDetection, ALADAnomalyDetectionComparison
from .anogan import AnoGANAnomalyDetection, AnoGANAnomalyDetectionComparison
from .cblof import CBLOFAnomalyDetection, CBLOFAnomalyDetectionComparison
from .cof import COFAnomalyDetection, COFAnomalyDetectionComparison
from .copod import COPODAnomalyDetection, COPODAnomalyDetectionComparison
from .deepsvdd import DeepSVDDAnomalyDetection, DeepSVDDAnomalyDetectionComparison
from .ecod import ECODAnomalyDetection, ECODAnomalyDetectionComparison
from .gmm import GMMAnomalyDetection, GMMAnomalyDetectionComparison
from .pca import PCAAnomalyDetection,PCAAnomalyDetectionComparison
from .rgraph import RGraphAnomalyDetection,RGraphAnomalyDetectionComparison
from .sampling import SamplingAnomalyDetection, SamplingAnomalyDetectionComparison
from .suod import SUODAnomalyDetection, SUODAnomalyDetectionComparison
from .rod import RODAnomalyDetection,RODAnomalyDetectionComparison
from .sos import SOSAnomalyDetection, SOSAnomalyDetectionComparison
from .sod import SODAnomalyDetection, SODAnomalyDetectionComparison
from .qmcd import QMCDAnomalyDetection,QMCDAnomalyDetectionComparison
from .so_gaal import SO_GAALAnomalyDetection,SO_GAALAnomalyDetectionComparison
from .ocsvm import OCSVMAnomalyDetection, OCSVMAnomalyDetectionComparison 
from .mo_gaal import MO_GAALAnomalyDetection, MO_GAALAnomalyDetectionComparison
from .mcd import MCDAnomalyDetection, MCDAnomalyDetectionComparison
from .lunar import LUNARAnomalyDetection, LUNARAnomalyDetectionComparison
from .lof import LOFAnomalyDetection, LOFAnomalyDetectionComparison
from .loda import LODAAnomalyDetection, LODAAnomalyDetectionComparison
from .hbos import HBOSAnomalyDetection, HBOSAnomalyDetectionComparison
from .iforest import IForestAnomalyDetection, IForestAnomalyDetectionComparison
from .iforestnne import INNEAnomalyDetection, INNEAnomalyDetectionComparison
from .kde import KDEAnomalyDetection, KDEAnomalyDetectionComparison
from .kpca import KPCAAnomalyDetection, KPCAAnomalyDetectionComparison
from .knn import KNNAnomalyDetection, KNNAnomalyDetectionComparison


models_ad = {
    'ABOD Anomaly Detection': ABODAnomalyDetection,
    'ALAD Anomaly Detection': ALADAnomalyDetection,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetection,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetection,
    'Connectivity-Based Outlier Factor': COFAnomalyDetection,
    'Copula Based Outlier Detector': COPODAnomalyDetection,
    'Deep One-Class Classification': DeepSVDDAnomalyDetection,
    'Empirical Cumulative Distribution': ECODAnomalyDetection,
    'Gaussian Mixture Model': GMMAnomalyDetection,
    'Principal Component Analysis': PCAAnomalyDetection,
    'R Graph' : RGraphAnomalyDetection,
    'Outlier detection based on Sampling': SamplingAnomalyDetection,
    'SUOD Anomaly Detection': SUODAnomalyDetection,
    'Rotation-based Outlier Detector': RODAnomalyDetection,
    'Stochastic Outlier Selection': SOSAnomalyDetection,
    'Subspace Outlier Detection': SODAnomalyDetection,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetection,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetection,
    'One-class SVM detector':OCSVMAnomalyDetection,
    'MO_GAAL Anomaly Detection': MO_GAALAnomalyDetection,
    'Minimum Covariance Determinant': MCDAnomalyDetection,
    'LUNAR Anomaly Detection': LUNARAnomalyDetection,
    'LOF Anomaly Detection': LOFAnomalyDetection,
    'LODA Anomaly Detection': LODAAnomalyDetection,
    'Histogram-based Outlier Detection': HBOSAnomalyDetection,
    'Isolation Forest': IForestAnomalyDetection,
    'Isolation NNE': INNEAnomalyDetection,
    'Kernel Density Estimation': KDEAnomalyDetection,
    'Kernel PCA': KPCAAnomalyDetection,
    'k-Nearest Neighbors': KNNAnomalyDetection
}

models_comparison_ad = {
    'ABOD Anomaly Detection': ABODAnomalyDetectionComparison,
    'ALAD Anomaly Detection': ALADAnomalyDetectionComparison,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetectionComparison,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetectionComparison,
    'Connectivity-Based Outlier Factor': COFAnomalyDetectionComparison,
    'Copula Based Outlier Detector': COPODAnomalyDetectionComparison,
    'Deep One-Class Classification': DeepSVDDAnomalyDetectionComparison,
    'Empirical Cumulative Distribution': ECODAnomalyDetectionComparison,
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison,
    'Principal Component Analysis': PCAAnomalyDetectionComparison,
    'R Graph' : RGraphAnomalyDetectionComparison,
    'Outlier detection based on Sampling': SamplingAnomalyDetectionComparison,
    'SUOD Anomaly Detection': SUODAnomalyDetectionComparison,
    'Rotation-based Outlier Detector': RODAnomalyDetectionComparison,
    'Stochastic Outlier Selection': SOSAnomalyDetectionComparison,
    'Subspace Outlier Detection': SODAnomalyDetectionComparison,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetectionComparison,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetectionComparison,
    'One-class SVM detector':OCSVMAnomalyDetectionComparison,
    'MO_GAAL Anomaly Detection': MO_GAALAnomalyDetectionComparison,
    'Minimum Covariance Determinant': MCDAnomalyDetectionComparison,
    'LUNAR Anomaly Detection': LUNARAnomalyDetectionComparison,
    'LOF Anomaly Detection': LOFAnomalyDetectionComparison,
    'LODA Anomaly Detection': LODAAnomalyDetectionComparison,
    'Histogram-based Outlier Detection': HBOSAnomalyDetectionComparison,
    'Isolation Forest': IForestAnomalyDetectionComparison,
    'Isolation NNE': INNEAnomalyDetectionComparison,
    'Kernel Density Estimation': KDEAnomalyDetectionComparison,
    'Kernel PCA': KPCAAnomalyDetectionComparison,
    'k-Nearest Neighbors': KNNAnomalyDetectionComparison

}



models_ad_default = {
    'ABOD Anomaly Detection': ABODAnomalyDetection,
    'ALAD Anomaly Detection': ALADAnomalyDetection,
    'Deep One-Class Classification': DeepSVDDAnomalyDetection,
    'Empirical Cumulative Distribution': ECODAnomalyDetection,
    'Gaussian Mixture Model': GMMAnomalyDetection,
    'Principal Component Analysis': PCAAnomalyDetection,
    'Stochastic Outlier Selection': SOSAnomalyDetection,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetection,
    'Histogram-based Outlier Detection': HBOSAnomalyDetection,
    'Isolation Forest': IForestAnomalyDetection,
    'Isolation NNE': INNEAnomalyDetection,
    'Kernel Density Estimation': KDEAnomalyDetection,
    'k-Nearest Neighbors': KNNAnomalyDetection
}

models_comparison_ad_default = {
    'ABOD Anomaly Detection': ABODAnomalyDetectionComparison,
    'ALAD Anomaly Detection': ALADAnomalyDetectionComparison,
    'Deep One-Class Classification': DeepSVDDAnomalyDetectionComparison,
    'Empirical Cumulative Distribution': ECODAnomalyDetectionComparison,
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison,
    'Principal Component Analysis': PCAAnomalyDetectionComparison,
    'Stochastic Outlier Selection': SOSAnomalyDetectionComparison,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetectionComparison,
    'Histogram-based Outlier Detection': HBOSAnomalyDetectionComparison,
    'Isolation Forest': IForestAnomalyDetectionComparison,
    'Isolation NNE': INNEAnomalyDetectionComparison,
    'Kernel Density Estimation': KDEAnomalyDetectionComparison,
    'k-Nearest Neighbors': KNNAnomalyDetectionComparison
}
