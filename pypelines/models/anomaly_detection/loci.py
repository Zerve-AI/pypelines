from ..model_base import PYODModelBase, PYODModelComparisonBase

loci_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ]
}

class LOCIAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'LOCI()'
        imports = '''from pyod.models.loci import LOCI\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LOCI', model_string, loci_hyperparams, imports,model_type)

class LOCIAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'LOCI()'
        imports = '''from pyod.models.loci import LOCI\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('LOCI', model_string, loci_hyperparams, imports,model_type)