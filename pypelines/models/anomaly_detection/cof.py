from ..model_base import PYODModelBase, PYODModelComparisonBase

cof_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_neighbors', 'min': 2, 'max': 20, 'step': 2},
    ],
    'categorical': [
    ]
}


class COFAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'COF()'
        imports = '''from pyod.models.cof import COF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('COF', model_string, cof_hyperparams, imports,model_type)

class COFAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'COF()'
        imports = '''from pyod.models.cof import COF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('COF', model_string, cof_hyperparams, imports,model_type)