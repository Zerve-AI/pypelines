from ..model_base import TSClusteringModelBase,TSClusteringModelComparisonBase

KernelKMeans_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 4, 'max': 20, 'step': 4},
    ],
    'categorical': [
    ]
}


class KernelKMeansTSClustering(TSClusteringModelBase):
    def __init__(self):
        model_string = 'TimeSeriesKernelKMeans()'
        imports = '''from sktime.clustering.kernel_k_means import TimeSeriesKernelKMeans\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKernelKMeans', model_string, KernelKMeans_TS_regression_hyperparams, imports,model_type)

class KernelKMeansTSClusteringComparison(TSClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesKernelKMeans()'
        imports = '''from sktime.clustering.kernel_k_means import TimeSeriesKernelKMeans\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKernelKMeans', model_string, KernelKMeans_TS_regression_hyperparams, imports,model_type)