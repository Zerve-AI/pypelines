from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase

agglomerative_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 3, 'max': 10, 'step': 1}
    ],
    'categorical': [
        {'search': False, 'name': 'metric', 'selected': ["euclidean"], 'values': ["euclidean", "l1", "l2","manhattan","cosine","precomputed"]},
        {'search': False, 'name': 'linkage', 'selected': ["ward"], 'values': ["ward", "average", "complete","single"]},
    ]
}

class AgglomerativeClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'AgglomerativeClustering()'
        imports = '''from sklearn.cluster import AgglomerativeClustering \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('AgglomerativeClustering', model_string, agglomerative_clustering_hyperparams, imports,model_type)


class AgglomerativeClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'AgglomerativeClustering()'
        imports = '''from sklearn.cluster import AgglomerativeClustering \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('AgglomerativeClustering', model_string, agglomerative_clustering_hyperparams, imports,model_type)
