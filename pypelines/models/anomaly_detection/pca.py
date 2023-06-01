from ..model_base import PYODModelBase, PYODModelComparisonBase

pca_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05}
    ],
    'categorical': [
        {'search': True, 'name': 'svd_solver', 'selected': ['auto'], 'values': ['auto', 'full', 'arpack', 'randomized']}

        
    ]
}

class PCAAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'PCA()'
        imports = '''from pyod.models.pca import PCA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('PCA', model_string, pca_hyperparams, imports,model_type)

class PCAAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'PCA()'
        imports = '''from pyod.models.pca import PCA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('PCA', model_string, pca_hyperparams, imports,model_type)