from ..model_base import TSClusteringModelBase,TSClusteringModelComparisonBase

KMediods_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 4, 'max': 20, 'step': 4},
    ],
    'categorical': [
        {'search': True, 'name': 'init_algorithm', 'selected': ['random'], 'values': ['kmeans++','random', 'forgy']},
        {'search': True, 'name': 'metric', 'selected': ['dtw'], 'values': ['dtw', 'euclidean', 'erp', 'edr', 'lcss', 
                                                                           'squared', 'ddtw', 'wdtw', 'wddtw']}]
}


class KMediodsTSClustering(TSClusteringModelBase):
    def __init__(self):
        model_string = 'TimeSeriesKMedoids()'
        imports = '''from sktime.clustering.k_medoids import TimeSeriesKMedoids\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKMedoids', model_string, KMediods_TS_regression_hyperparams, imports,model_type)

class KMediodsTSClusteringComparison(TSClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesKMedoids()'
        imports = '''from sktime.clustering.k_medoids import TimeSeriesKMedoids\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKMedoids', model_string, KMediods_TS_regression_hyperparams, imports,model_type)