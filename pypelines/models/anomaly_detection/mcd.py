from ..model_base import PYODModelBase, PYODModelComparisonBase

mcd_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ],
    'categorical': [
        {'search': True, 'name': 'store_precision', 'selected': [True], 'values': [True,False]}
        
    ]
}

class MCDAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'MCD()'
        imports = '''from pyod.models.mcd import MCD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('MCD', model_string, mcd_hyperparams, imports,model_type)

class MCDAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'MCD()'
        imports = '''from pyod.models.mcd import MCD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('MCD', model_string, mcd_hyperparams, imports,model_type)