from ..model_base import PYODModelBase, PYODModelComparisonBase

copod_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'contamination', 'min': 0., 'max': 1, 'step': 0.25},
    ],
    'categorical': [
    ]

}


class COPODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'COPOD()'
        imports = '''from pyod.models.copod import COPOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('COPOD', model_string, copod_hyperparams, imports,model_type)

class COPODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'COPOD()'
        imports = '''from pyod.models.copod import COPOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('COPOD', model_string, copod_hyperparams, imports,model_type)