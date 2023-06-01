from ..model_base import PYODModelBase, PYODModelComparisonBase

loda_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'contamination', 'min': 0, 'max': 0.5, 'step': 0.1}
    ]
}

class LODAAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'LODA()'
        imports = '''from pyod.models.loda import LODA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LODA', model_string, loda_hyperparams, imports,model_type)

class LODAAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'LODA()'
        imports = '''from pyod.models.loda import LODA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LODA', model_string, loda_hyperparams, imports,model_type)