from ..model_base import PYODModelBase, PYODModelComparisonBase

sod_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 0.8, 'step': 0.5},
        {'search': True, 'name': 'n_neighbors', 'min': 2, 'max': 20, 'step':5}       
    ]
}

class SODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'SOD()'
        imports = '''from pyod.models.sod import SOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SOD', model_string, sod_hyperparams, imports,model_type)

class SODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'SOD()'
        imports = '''from pyod.models.sod import SOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SOD', model_string, sod_hyperparams, imports,model_type)