from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

hdbscan_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'min_cluster_size', 'min': 5, 'max': 20, 'step': 5}
    ],
    'categorical': [
        {'search': False, 'name': 'cluster_selection_method', 'selected': ["eom"], 'values': ["eom", "leaf"]},
        {'search': False, 'name': 'algorithm', 'selected': ["auto"], 'values': ["auto", "ball_tree", "kd_tree","brute"]},
    ]
}

class HDBSCANClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'HDBSCAN()'
        imports = '''from sklearn.cluster import HDBSCAN \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('HDBSCAN', model_string, hdbscan_clustering_hyperparams, imports,model_type)


class HDBSCANClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'HDBSCAN()'
        imports = '''from sklearn.cluster import HDBSCAN \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('HDBSCAN', model_string, hdbscan_clustering_hyperparams, imports,model_type)

