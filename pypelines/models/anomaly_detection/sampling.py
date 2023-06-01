from ..model_base import PYODModelBase, PYODModelComparisonBase

sampling_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': True, 'name': 'subset_size', 'min': 10, 'max': 20, 'step': 15}
    ],
    'categorical': [
        {'search': True, 'name': 'metric', 'selected': ['minkowski'], 'values': ['braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']}
        
    ]
}

class SamplingAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'Sampling()'
        imports = '''from pyod.models.sampling import Sampling\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('Sampling', model_string, sampling_hyperparams, imports,model_type)

class SamplingAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'Sampling()'
        imports = '''from pyod.models.sampling import Sampling\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('Sampling', model_string, sampling_hyperparams, imports,model_type)