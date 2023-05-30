from .abod import ABODAnomalyDetection, ABODAnomalyDetectionComparison
from .alad import ALADAnomalyDetection, ALADAnomalyDetectionComparison
from .anogan import AnoGANAnomalyDetection, AnoGANAnomalyDetectionComparison
from .autoencoder import AutoEncoderAnomalyDetection, AutoEncoderAnomalyDetectionComparison
from .autoencoder_torch import AutoEncoderTorchAnomalyDetection, AutoEncoderTorchAnomalyDetectionComparison
from .cblof import CBLOFAnomalyDetection, CBLOFAnomalyDetectionComparison
from .cof import COFAnomalyDetection, COFAnomalyDetectionComparison
from .cd import CDAnomalyDetection, CDAnomalyDetectionComparison
from .copod import COPODAnomalyDetection, COPODAnomalyDetectionComparison

models_ad = {
    'ABOD Anomaly Detection': ABODAnomalyDetection,
    'ALAD Anomaly Detection': ALADAnomalyDetection,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetection,
    'Autoencoder Anomaly Detection': AutoEncoderAnomalyDetection,
    'Autoencoder_Torch Anomaly Detection': AutoEncoderTorchAnomalyDetection,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetection,
    'Connectivity-Based Outlier Factor': COFAnomalyDetection,
    'Cooks Distance Outlier Factor': CDAnomalyDetection,
    'Copula Based Outlier Detector': COPODAnomalyDetection
}

models_comparison_ad = {
    'ABOD Anomaly Detection': ABODAnomalyDetectionComparison,
    'ALAD Anomaly Detection': ALADAnomalyDetectionComparison,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetectionComparison,
    'Autoencoder Anomaly Detection': AutoEncoderAnomalyDetectionComparison,
    'Autoencoder_Torch Anomaly Detection': AutoEncoderTorchAnomalyDetectionComparison,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetectionComparison,
    'Connectivity-Based Outlier Factor': COFAnomalyDetectionComparison,
    'Cooks Distance Outlier Factor': CDAnomalyDetectionComparison,
    'Copula Based Outlier Detector': COPODAnomalyDetectionComparison
}



models_ad_default = {
    'ABOD Anomaly Detection': ABODAnomalyDetection,
    'ALAD Anomaly Detection': ALADAnomalyDetection,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetection,
    'Autoencoder Anomaly Detection': AutoEncoderAnomalyDetection,
    'Autoencoder_Torch Anomaly Detection': AutoEncoderTorchAnomalyDetection,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetection,
    'Connectivity-Based Outlier Factor': COFAnomalyDetection,
    'Cooks Distance Outlier Factor': CDAnomalyDetection,
    'Copula Based Outlier Detector': COPODAnomalyDetection
}

models_comparison_ad_default = {
    'ABOD Anomaly Detection': ABODAnomalyDetectionComparison,
    'ALAD Anomaly Detection': ALADAnomalyDetectionComparison,
    'AnoGAN Anomaly Detection': AnoGANAnomalyDetectionComparison,
    'Autoencoder Anomaly Detection': AutoEncoderAnomalyDetectionComparison,
    'Autoencoder_Torch Anomaly Detection': AutoEncoderTorchAnomalyDetectionComparison,
    'Clustering Based Local Outlier Factor': CBLOFAnomalyDetectionComparison,
    'Connectivity-Based Outlier Factor': COFAnomalyDetectionComparison,
    'Cooks Distance Outlier Factor': CDAnomalyDetectionComparison,
    'Copula Based Outlier Detector': COPODAnomalyDetectionComparison
}