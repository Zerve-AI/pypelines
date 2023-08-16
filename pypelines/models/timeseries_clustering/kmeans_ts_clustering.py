from ..model_base import TSClusteringModelBase,TSClusteringModelComparisonBase

KMeans_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 4, 'max': 20, 'step': 4},
    ],
    'categorical': [
        {'search': True, 'name': 'init_algorithm', 'selected': ['random'], 'values': ['kmeans++','random', 'forgy']},
        {'search': True, 'name': 'metric', 'selected': ['dtw'], 'values': ['dtw', 'euclidean', 'erp', 'edr', 'lcss', 
                                                                           'squared', 'ddtw', 'wdtw', 'wddtw']}]
}


class KMeansTSClustering(TSClusteringModelBase):
    def __init__(self):
        model_string = 'TimeSeriesKMeans()'
        imports = '''from sktime.clustering.k_means import TimeSeriesKMeans\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKMeans', model_string, KMeans_TS_regression_hyperparams, imports,model_type)

class KMeansTSClusteringComparison(TSClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesKMeans()'
        imports = '''from sktime.clustering.k_means import TimeSeriesKMeans\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKMeans', model_string, KMeans_TS_regression_hyperparams, imports,model_type)