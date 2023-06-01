from ..model_base import PYODModelBase, PYODModelComparisonBase

mad_hyperparams = {
    'categorical': [
        {'search': False, 'name': 'labels_', 'selected': [0], 'values': [0,1]}
        
    ]
}

class MADAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'MAD()'
        imports = '''from pyod.models.mad import MAD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('MAD', model_string, mad_hyperparams, imports,model_type)

class MADAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'MAD()'
        imports = '''from pyod.models.mad import MAD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('MAD', model_string, mad_hyperparams, imports,model_type)