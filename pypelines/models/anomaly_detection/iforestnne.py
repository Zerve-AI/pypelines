from ..model_base import PYODModelBase, PYODModelComparisonBase

inne_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 500, 'step': 100},
    ],
    'categorical': [
    ]
}

class INNEAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'INNE()'
        imports = '''from pyod.models.inne import INNE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('INNE', model_string, inne_hyperparams, imports,model_type)

class INNEAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'INNE()'
        imports = '''from pyod.models.inne import INNE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('INNE', model_string, inne_hyperparams, imports,model_type)