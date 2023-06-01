from .abod import ABODAnomalyDetection, ABODAnomalyDetectionComparison
from .alad import ALADAnomalyDetection, ALADAnomalyDetectionComparison
from .anogan import AnoGANAnomalyDetection, AnoGANAnomalyDetectionComparison
from .cblof import CBLOFAnomalyDetection, CBLOFAnomalyDetectionComparison
from .cof import COFAnomalyDetection, COFAnomalyDetectionComparison
from .cd import CDAnomalyDetection, CDAnomalyDetectionComparison
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
from .vae import VAEAnomalyDetection, VAEAnomalyDetectionComparison
from .ocsvm import OCSVMAnomalyDetection, OCSVMAnomalyDetectionComparison 
from .loci import LOCIAnomalyDetection, LOCIAnomalyDetectionComparison
from .mo_gaal import MO_GAALAnomalyDetection, MO_GAALAnomalyDetectionComparison
from .mcd import MCDAnomalyDetection, MCDAnomalyDetectionComparison
from .mad import MADAnomalyDetection, MADAnomalyDetectionComparison
from .lscp import LSCPAnomalyDetection, LSCPAnomalyDetectionComparison
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
    'Cooks Distance Outlier Factor': CDAnomalyDetection,
    'Copula Based Outlier Detector': COPODAnomalyDetection,
    'Deep One-Class Classification': DeepSVDDAnomalyDetection,
    'Empirical Cumulative Distribution': ECODAnomalyDetection,
    'Gaussian Mixture Model': GMMAnomalyDetection,
    'Principal Component Analysis': PCAAnomalyDetection,
    'R Graph' : RGraphAnomalyDetection,
    'Outlier detection based on Sampling': SamplingAnomalyDetection,
    'SUOD': SUODAnomalyDetection,
    'Rotation-based Outlier Detector': RODAnomalyDetection,
    'Stochastic Outlier Selection': SOSAnomalyDetection,
#     'Subspace Outlier Detection': SODAnomalyDetection,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetection,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetection,
#    'VAE Unsupervised Outlier Detection':VAEAnomalyDetection,
    'One-class SVM detector':OCSVMAnomalyDetection,
#     'Local Correlation Integral': LOCIAnomalyDetection,
    'MO_GAAL': MO_GAALAnomalyDetection,
    'MCD': MCDAnomalyDetection,
#     'MAD': MADAnomalyDetection,
#     'LSCP': LSCPAnomalyDetection,
#     'LUNAR': LUNARAnomalyDetection,
    'LOF': LOFAnomalyDetection,
    'LODA': LODAAnomalyDetection
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
    'Cooks Distance Outlier Factor': CDAnomalyDetectionComparison,
    'Copula Based Outlier Detector': COPODAnomalyDetectionComparison,
    'Deep One-Class Classification': DeepSVDDAnomalyDetectionComparison,
    'Empirical Cumulative Distribution': ECODAnomalyDetectionComparison,
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison,
    'Principal Component Analysis': PCAAnomalyDetectionComparison,
    'R Graph' : RGraphAnomalyDetectionComparison,
    'Outlier detection based on Sampling': SamplingAnomalyDetectionComparison,
    'SUOD': SUODAnomalyDetectionComparison,
    'Rotation-based Outlier Detector': RODAnomalyDetectionComparison,
    'Stochastic Outlier Selection': SOSAnomalyDetectionComparison,
#    'Subspace Outlier Detection': SODAnomalyDetectionComparison,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetectionComparison,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetectionComparison,
#    'VAE Unsupervised Outlier Detection':VAEAnomalyDetectionComparison,
    'One-class SVM detector':OCSVMAnomalyDetectionComparison,
#    'Local Correlation Integral': LOCIAnomalyDetectionComparison,
    'MO_GAAL': MO_GAALAnomalyDetectionComparison,
    'MCD': MCDAnomalyDetectionComparison,
#    'MAD': MADAnomalyDetectionComparison,
#    'LSCP': LSCPAnomalyDetectionComparison,
#    'LUNAR': LUNARAnomalyDetectionComparison,
    'LOF': LOFAnomalyDetectionComparison,
    'LODA': LODAAnomalyDetectionComparison
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
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetection,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetection,
    'Connectivity-Based Outlier Factor': COFAnomalyDetection,
    'Cooks Distance Outlier Factor': CDAnomalyDetection,
    'Copula Based Outlier Detector': COPODAnomalyDetection,
    'Deep One-Class Classification': DeepSVDDAnomalyDetection,
    'Empirical Cumulative Distribution': ECODAnomalyDetection,
    'Gaussian Mixture Model': GMMAnomalyDetection,
    'Principal Component Analysis': PCAAnomalyDetection,
    'R Graph' : RGraphAnomalyDetection,
    'Outlier detection based on Sampling': SamplingAnomalyDetection,
    'SUOD': SUODAnomalyDetection,
    'Rotation-based Outlier Detector': RODAnomalyDetection,
    'Stochastic Outlier Selection': SOSAnomalyDetection,
#     'Subspace Outlier Detection': SODAnomalyDetection,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetection,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetection,
#    'VAE Unsupervised Outlier Detection':VAEAnomalyDetection,
    'One-class SVM detector':OCSVMAnomalyDetection,
#     'Local Correlation Integral': LOCIAnomalyDetection,
    'MO_GAAL': MO_GAALAnomalyDetection,
    'MCD': MCDAnomalyDetection,
#     'MAD': MADAnomalyDetection,
#     'LSCP': LSCPAnomalyDetection,
#     'LUNAR': LUNARAnomalyDetection,
    'LOF': LOFAnomalyDetection,
    'LODA': LODAAnomalyDetection
    'Histogram-based Outlier Detection': HBOSAnomalyDetection,
    'Isolation Forest': IForestAnomalyDetection,
    'Isolation NNE': INNEAnomalyDetection,
    'Kernel Density Estimation': KDEAnomalyDetection,
    'Kernel PCA': KPCAAnomalyDetection,
    'k-Nearest Neighbors': KNNAnomalyDetection
}

models_comparison_ad_default = {
    'ABOD Anomaly Detection': ABODAnomalyDetectionComparison,
    'ALAD Anomaly Detection': ALADAnomalyDetectionComparison,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetectionComparison,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetectionComparison,
    'Connectivity-Based Outlier Factor': COFAnomalyDetectionComparison,
    'Cooks Distance Outlier Factor': CDAnomalyDetectionComparison,
    'Copula Based Outlier Detector': COPODAnomalyDetectionComparison,
    'Deep One-Class Classification': DeepSVDDAnomalyDetectionComparison,
    'Empirical Cumulative Distribution': ECODAnomalyDetectionComparison,
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison,
    'Principal Component Analysis': PCAAnomalyDetectionComparison,
    'R Graph' : RGraphAnomalyDetectionComparison,
    'Outlier detection based on Sampling': SamplingAnomalyDetectionComparison,
    'SUOD': SUODAnomalyDetectionComparison,
    'Rotation-based Outlier Detector': RODAnomalyDetectionComparison,
    'Stochastic Outlier Selection': SOSAnomalyDetectionComparison,
#    'Subspace Outlier Detection': SODAnomalyDetectionComparison,
    'Quasi-Monte Carlo Discrepancy outlier detection':QMCDAnomalyDetectionComparison,
    'Single-Objective Generative Adversarial Active Learning':SO_GAALAnomalyDetectionComparison,
#    'VAE Unsupervised Outlier Detection':VAEAnomalyDetectionComparison,
    'One-class SVM detector':OCSVMAnomalyDetectionComparison,
#    'Local Correlation Integral': LOCIAnomalyDetectionComparison,
    'MO_GAAL': MO_GAALAnomalyDetectionComparison,
    'MCD': MCDAnomalyDetectionComparison,
#    'MAD': MADAnomalyDetectionComparison,
#    'LSCP': LSCPAnomalyDetectionComparison,
#    'LUNAR': LUNARAnomalyDetectionComparison,
    'LOF': LOFAnomalyDetectionComparison,
    'LODA': LODAAnomalyDetectionComparison
    'Histogram-based Outlier Detection': HBOSAnomalyDetectionComparison,
    'Isolation Forest': IForestAnomalyDetectionComparison,
    'Isolation NNE': INNEAnomalyDetectionComparison,
    'Kernel Density Estimation': KDEAnomalyDetectionComparison,
    'Kernel PCA': KPCAAnomalyDetectionComparison,
    'k-Nearest Neighbors': KNNAnomalyDetectionComparison
}