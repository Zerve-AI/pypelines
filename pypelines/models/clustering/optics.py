from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

optics_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'min_samples', 'min': 0.1, 'max': 0.9, 'step': 0.1}
    ],
    'categorical': [
        {'search': False, 'name': 'metric', 'selected': ["euclidean"], 'values': ["euclidean", "l1", "l2","manhattan","cosine","cityblock"]},
        {'search': False, 'name': 'algorithm', 'selected': ["auto"], 'values': ["auto", "ball_tree", "kd_tree","brute"]},
    ]
}

class OPTICSClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'OPTICS()'
        imports = '''from sklearn.cluster import OPTICS \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('OPTICS', model_string, optics_clustering_hyperparams, imports,model_type)


class OPTICSClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'OPTICS()'
        imports = '''from sklearn.cluster import OPTICS \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('OPTICS', model_string, optics_clustering_hyperparams, imports,model_type)

