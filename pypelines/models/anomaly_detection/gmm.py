from ..model_base import PYODModelBase, PYODModelComparisonBase

gmm_hyperparams = {
    'categorical': [
        {'search': True, 'name': 'covariance_type', 'selected': ['full'], 'values': ['full', 'tied', 'diag', 'spherical']},
    ]

}

class GMMAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'GMM()'
        imports = '''from pyod.models.gmm import GMM\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('GMM', model_string, gmm_hyperparams, imports,model_type)

class GMMAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'GMM()'
        imports = '''from pyod.models.gmm import GMM\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('GMM', model_string, gmm_hyperparams, imports,model_type)