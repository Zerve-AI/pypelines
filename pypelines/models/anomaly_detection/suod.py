from ..model_base import PYODModelBase, PYODModelComparisonBase

suod_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'target_dim_frac', 'min': 0.1, 'max': 1, 'step': 0.5}
    ],
    'categorical': [
        {'search': True, 'name': 'jl_method', 'selected': ['basic'], 'values': ['basic','discrete','circulant','toeplitz']}
        
    ]
}

class SUODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'SUOD()'
        imports = '''from pyod.models.suod import SUOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SUOD', model_string, suod_hyperparams, imports,model_type)

class SUODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'SUOD()'
        imports = '''from pyod.models.suod import SUOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SUOD', model_string, suod_hyperparams, imports,model_type)