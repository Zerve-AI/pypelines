from ..model_base import TSClusteringModelBase,TSClusteringModelComparisonBase

KShapes_TS_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 4, 'max': 20, 'step': 4},
    ],
    'categorical': [
    ]
}


class KShapesTSClustering(TSClusteringModelBase):
    def __init__(self):
        model_string = 'TimeSeriesKShapes()'
        imports = '''from sktime.clustering.k_shapes import TimeSeriesKShapes\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKShapes', model_string, KShapes_TS_regression_hyperparams, imports,model_type)

class KShapesTSClusteringComparison(TSClusteringModelComparisonBase):
    def __init__(self):
        model_string = 'TimeSeriesKShapes()'
        imports = '''from sktime.clustering.k_shapes import TimeSeriesKShapes\nfrom sklearn.model_selection import GridSearchCV\nimport matplotlib.pyplot as plt\nfrom sktime.clustering.utils.plotting._plot_partitions import plot_cluster_algorithm'''
        model_type ='Clustering'
        super().__init__('TimeSeriesKShapes', model_string, KShapes_TS_regression_hyperparams, imports,model_type)