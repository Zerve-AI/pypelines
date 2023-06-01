from ..model_base import PYODModelBase, PYODModelComparisonBase

sos_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ],
    'categorical': [
        {'search': True, 'name': 'metric', 'selected': ['euclidean'], 'values': ['euclidean','braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']}
        
    ]
}

class SOSAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'SOS()'
        imports = '''from pyod.models.sos import SOS\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SOS', model_string, sos_hyperparams, imports,model_type)

class SOSAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'SOS()'
        imports = '''from pyod.models.sos import SOS\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('SOS', model_string, sos_hyperparams, imports,model_type)