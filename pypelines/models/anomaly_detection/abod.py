from ..model_base import PYODModelBase, PYODModelComparisonBase

abod_hyperparams = {
    'numerical': [
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