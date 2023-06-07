from ..model_base import PYODModelBase, PYODModelComparisonBase

abod_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'contamination', 'min': 0., 'max': 1, 'step': 0.25},
        {'search': False, 'name': 'n_neighbors', 'min': 2, 'max': 20, 'step': 10},
    ],
    'categorical': [
    ]
}


class ABODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'ABOD()'
        imports = '''from pyod.models.abod import ABOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ABOD', model_string, abod_hyperparams, imports,model_type)

class ABODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'ABOD()'
        imports = '''from pyod.models.abod import ABOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ABOD', model_string, abod_hyperparams, imports,model_type)