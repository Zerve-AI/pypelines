from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

dbscan_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'eps', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'min_samples', 'min': 5, 'max': 20, 'step': 5}
    ],
    'categorical': [
        {'search': False, 'name': 'metric', 'selected': ["euclidean"], 'values': ["euclidean", "l1", "l2","manhattan","cosine","precomputed"]},
        {'search': False, 'name': 'algorithm', 'selected': ["auto"], 'values': ["auto", "ball_tree", "kd_tree","brute"]},
    ]
}

class DBSCANClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'DBSCAN()'
        imports = '''from sklearn.cluster import DBSCAN \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('DBSCAN', model_string, dbscan_clustering_hyperparams, imports,model_type)


class DBSCANClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'DBSCAN()'
        imports = '''from sklearn.cluster import DBSCAN \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('DBSCAN', model_string, dbscan_clustering_hyperparams, imports,model_type)

