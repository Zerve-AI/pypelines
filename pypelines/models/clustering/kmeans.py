from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase


kmeans_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 3, 'max': 10, 'step': 1},
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 200, 'step': 50}
    ],
    'categorical': [
        {'search': False, 'name': 'algorithm', 'selected': ["lloyd"], 'values': ["lloyd", "elkan", "auto","full"]}
    ]
}

class KMeansClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'KMeans()'
        imports = '''from sklearn.cluster import KMeans \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('KMeans', model_string, kmeans_clustering_hyperparams, imports,model_type)


class KMeansClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'KMeans()'
        imports = '''from sklearn.cluster import KMeans \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('KMeans', model_string, kmeans_clustering_hyperparams, imports,model_type)
