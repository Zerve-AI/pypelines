from ..model_base import PYODModelBase, PYODModelComparisonBase

ocsvm_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ],
    'categorical': [
        {'search': True, 'name': 'kernel', 'selected': ['rbf'], 'values': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']}

        
    ]
}

class OCSVMAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'OCSVM()'
        imports = '''from pyod.models.ocsvm import OCSVM\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('OCSVM', model_string, ocsvm_hyperparams, imports,model_type)

class OCSVMAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'OCSVM()'
        imports = '''from pyod.models.ocsvm import OCSVM\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('OCSVM', model_string, ocsvm_hyperparams, imports,model_type)