from ..model_base import PYODModelBase, PYODModelComparisonBase

copod_hyperparams = {

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