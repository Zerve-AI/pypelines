from ..model_base import PYODModelBase, PYODModelComparisonBase

lof_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ],
    'categorical': [
        {'search': True, 'name': 'algorithm', 'selected': ['auto'], 'values': ['auto', 'ball_tree', 'kd_tree', 'brute']}

        
    ]
}

class LOFAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'LOF()'
        imports = '''from pyod.models.lof import LOF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LOF', model_string, lof_hyperparams, imports,model_type)

class LOFAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'LOF()'
        imports = '''from pyod.models.lof import LOF\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LOF', model_string, lof_hyperparams, imports,model_type)