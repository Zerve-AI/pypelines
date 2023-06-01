from ..model_base import PYODModelBase, PYODModelComparisonBase

hbos_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_bins', 'min': 5, 'max': 50, 'step': 5},
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 0.25, 'step': 0.99},
    ],
    'categorical': [
    ]

}

class HBOSAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'HBOS()'
        imports = '''from pyod.models.hbos import HBOS\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('HBOS', model_string, hbos_hyperparams, imports,model_type)

class HBOSAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'HBOS()'
        imports = '''from pyod.models.hbos import HBOS\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('HBOS', model_string, hbos_hyperparams, imports,model_type)