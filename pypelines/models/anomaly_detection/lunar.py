from ..model_base import PYODModelBase, PYODModelComparisonBase

lunar_hyperparams = {
    'numerical': [
        {'search': False, 'val_size': 'contamination', 'min': 0, 'max': 1, 'step': 0.1},
    ],
    'categorical': [
        {'search': False, 'name': 'model_type', 'selected': ['WEIGHT'], 'values': ['WEIGHT', 'SCORE']}
        
    ]
}

class LUNARAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'LUNAR()'
        imports = '''from pyod.models.lunar import LUNAR\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LUNAR', model_string, lunar_hyperparams, imports,model_type)

class LUNARAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'LUNAR()'
        imports = '''from pyod.models.lunar import LUNAR\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LUNAR', model_string, lunar_hyperparams, imports,model_type)
