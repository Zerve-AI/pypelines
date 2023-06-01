from ..model_base import PYODModelBase, PYODModelComparisonBase

qmcd_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ]
}

class QMCDAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'QMCD()'
        imports = '''from pyod.models.qmcd import QMCD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('QMCD', model_string, qmcd_hyperparams, imports,model_type)

class QMCDAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'QMCD()'
        imports = '''from pyod.models.qmcd import QMCD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('QMCD', model_string, qmcd_hyperparams, imports,model_type)