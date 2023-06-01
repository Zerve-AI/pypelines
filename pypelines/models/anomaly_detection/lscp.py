from ..model_base import PYODModelBase, PYODModelComparisonBase

lscp_hyperparams = {
        'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'local_max_features', 'min': 0.5, 'max': 1, 'step': 0.5},
        {'search': True, 'name': 'detector_list', 'min': 2, 'max': 10, 'step': 1}
    ]
}

class LSCPAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'LSCP()'
        imports = '''from pyod.models.lscp import LSCP\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LSCP', model_string, lscp_hyperparams, imports,model_type)

class LSCPAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'LSCP()'
        imports = '''from pyod.models.lscp import LSCP\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LSCP', model_string, lscp_hyperparams, imports,model_type)