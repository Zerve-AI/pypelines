from ..model_base import PYODModelBase, PYODModelComparisonBase

rod_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'contamination', 'min': 0, 'max': 0.5, 'step': 0.1}
    ],
    'categorical': [
        {'search': False, 'name': 'parallel_execution', 'selected': [False], 'values': [True,False]}
        
    ]
}

class RODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'ROD()'
        imports = '''from pyod.models.rod import ROD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ROD', model_string, rod_hyperparams, imports,model_type)

class RODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'ROD()'
        imports = '''from pyod.models.rod import ROD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ROD', model_string, rod_hyperparams, imports,model_type)