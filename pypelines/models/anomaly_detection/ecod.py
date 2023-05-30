from ..model_base import PYODModelBase, PYODModelComparisonBase

ecod_hyperparams = {

}

class ECODAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'ECOD()'
        imports = '''from pyod.models.ecod import ECOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ECOD', model_string, ecod_hyperparams, imports,model_type)

class ECODAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'ECOD()'
        imports = '''from pyod.models.ecod import ECOD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ECOD', model_string, ecod_hyperparams, imports,model_type)