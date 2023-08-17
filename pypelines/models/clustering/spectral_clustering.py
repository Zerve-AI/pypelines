from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

spectral_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 3, 'max': 10, 'step': 1}
    ],
    'categorical': [
        {'search': False, 'name': 'eigen_solver', 'selected': ["arpack"], 'values': ["lobpcg", "arpack", "amg"]},
        {'search': False, 'name': 'affinity', 'selected': ["rbf"], 'values': ["nearest_neighbors", "rbf", "precomputed","precomputed_nearest_neighbors"]}
    ]
}

class SpectralClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'SpectralClustering()'
        imports = '''from sklearn.cluster import SpectralClustering \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('SpectralClustering', model_string, spectral_clustering_hyperparams, imports,model_type)


class SpectralClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'SpectralClustering()'
        imports = '''from sklearn.cluster import SpectralClustering \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('SpectralClustering', model_string, spectral_clustering_hyperparams, imports,model_type)
