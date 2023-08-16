from ..model_base import ClusteringModelBase, ClusteringModelComparisonBase


mean_shift_clustering_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'max_iter', 'min': 100, 'max': 400, 'step': 50}
    ],
    'categorical': [
    ]
}

class MeanShiftClustering(ClusteringModelBase):
    def __init__(self):
        model_string = 'MeanShift()'
        imports = '''from sklearn.cluster import MeanShift \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('MeanShift', model_string, mean_shift_clustering_hyperparams, imports, model_type)


class MeanShiftClusteringComparison(ClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'MeanShift()'
        imports = '''from sklearn.cluster import MeanShift \nfrom sklearn.metrics import silhouette_samples, silhouette_score \nimport matplotlib.pyplot as plt \nimport matplotlib.cm as cm'''
        model_type='Clustering'
        super().__init__('MeanShift', model_string, mean_shift_clustering_hyperparams, imports, model_type)
