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
    'Gaussian Mixture Model': GMMAnomalyDetection
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
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison
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
    'Gaussian Mixture Model': GMMAnomalyDetection
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
    'Gaussian Mixture Model': GMMAnomalyDetectionComparison
}