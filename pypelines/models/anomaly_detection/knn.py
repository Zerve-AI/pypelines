from ..model_base import PYODModelBase, PYODModelComparisonBase

knn_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'leaf_size', 'min': 10, 'max': 50, 'step': 10},
    ],
    'categorical': [
        {'search': True, 'name': 'method', 'selected': ['largest'], 'values': ['largest', 'mean', 'median']},
        {'search': True, 'name': 'algorithm', 'selected': ['auto'], 'values': ['auto', 'ball_tree', 'kd_tree', 'brute']},
    ]
}

class KNNAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'KNN()'
        imports = '''from pyod.models.knn import KNN\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KNN', model_string, knn_hyperparams, imports,model_type)

class KNNAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'KNN()'
        imports = '''from pyod.models.knn import KNN\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KNN', model_string, knn_hyperparams, imports,model_type)