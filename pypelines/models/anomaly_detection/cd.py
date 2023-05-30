from ..model_base import PYODModelBase, PYODModelComparisonBase

cd_hyperparams = {

}


class CDAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'CD()'
        imports = '''from pyod.models.cd import CD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('CD', model_string, cd_hyperparams, imports,model_type)

class CDAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'CD()'
        imports = '''from pyod.models.cd import CD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('CD', model_string, cd_hyperparams, imports,model_type)