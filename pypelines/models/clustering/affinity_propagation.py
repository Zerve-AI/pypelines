from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase


affinity_propagation_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'convergence_iter', 'min': 15, 'max': 50, 'step': 20},
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 200, 'step': 50}
    ],
    'categorical': [
        {'search': False, 'name': 'affinity', 'selected': ["euclidean"], 'values': ["precomputed", "euclidean"]}
    ]
}

class AffinityPropagationClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'AffinityPropagation()'
        imports = '''from sklearn.cluster import AffinityPropagation \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('AffinityPropagation', model_string, affinity_propagation_clustering_hyperparams, imports, model_type)


class AffinityPropagationClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'AffinityPropagation()'
        imports = '''from sklearn.cluster import AffinityPropagation \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('AffinityPropagation', model_string, affinity_propagation_clustering_hyperparams, imports, model_type)
