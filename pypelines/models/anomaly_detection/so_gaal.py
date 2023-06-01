from ..model_base import PYODModelBase, PYODModelComparisonBase

so_gaal_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'stop_epochs', 'min': 10, 'max': 20, 'step': 15}
    ]
}

class SO_GAALAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'SO_GAAL()'
        imports = '''from pyod.models.so_gaal import SO_GAAL\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SO_GAAL', model_string, so_gaal_hyperparams, imports,model_type)

class SO_GAALAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'SO_GAAL()'
        imports = '''from pyod.models.so_gaal import SO_GAAL\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SO_GAAL', model_string, so_gaal_hyperparams, imports,model_type)