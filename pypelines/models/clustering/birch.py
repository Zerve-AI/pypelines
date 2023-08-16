from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

birch_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 3, 'max': 10, 'step': 1}
    ],
    'categorical': [
    ]
}

class BirchClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'Birch()'
        imports = '''from sklearn.cluster import Birch \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('Birch', model_string, birch_clustering_hyperparams, imports,model_type)


class BirchClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'Birch()'
        imports = '''from sklearn.cluster import Birch \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('Birch', model_string, birch_clustering_hyperparams, imports,model_type)
