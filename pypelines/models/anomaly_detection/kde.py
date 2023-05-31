from ..model_base import PYODModelBase, PYODModelComparisonBase

kde_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'leaf_size', 'min': 10, 'max': 50, 'step': 10},
    ],
    'categorical': [
        {'search': True, 'name': 'algorithm', 'selected': ['auto'], 'values': ['auto', 'ball_tree', 'kd_tree']},
    ]
}

class KDEAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'KDE()'
        imports = '''from pyod.models.kde import KDE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KDE', model_string, kde_hyperparams, imports,model_type)

class KDEAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'KDE()'
        imports = '''from pyod.models.kde import KDE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KDE', model_string, kde_hyperparams, imports,model_type)