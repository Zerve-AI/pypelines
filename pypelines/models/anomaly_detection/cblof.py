from ..model_base import PYODModelBase, PYODModelComparisonBase

cblof_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_clusters', 'min': 2, 'max': 20, 'step': 2},
        {'search': True, 'name': 'alpha', 'min': 0.5, 'max': 1, 'step': 0.1},
        {'search': True, 'name': 'beta', 'min': 1, 'max': 100, 'step': 20},
    ],
    'categorical': [
    ]
}


class CBLOFAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'CBLOF()'
        imports = '''from pyod.models.cblof import CBLOF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('CBLOF', model_string, cblof_hyperparams, imports,model_type)

class CBLOFAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'CBLOF()'
        imports = '''from pyod.models.cblof import CBLOF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('CBLOF', model_string, cblof_hyperparams, imports,model_type)