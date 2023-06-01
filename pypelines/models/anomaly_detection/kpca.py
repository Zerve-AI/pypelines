from ..model_base import PYODModelBase, PYODModelComparisonBase

kpca_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0, 'max': 1, 'step': 0.25},
    ],
    'categorical': [
        {'search': True, 'name': 'kernel', 'selected': ['rbf'], 'values': ['linear', 'poly', 'rbf', 'sigmoid', 'cosine', 'precomputed']},
        {'search': True, 'name': 'eigen_solver', 'selected': ['auto'], 'values': ['auto', 'dense', 'arpack', 'randomized']},
    ]
}

class KPCAAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'KPCA()'
        imports = '''from pyod.models.kpca import KPCA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KPCA', model_string, kpca_hyperparams, imports,model_type)

class KPCAAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'KPCA()'
        imports = '''from pyod.models.kpca import KPCA\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('KPCA', model_string, kpca_hyperparams, imports,model_type)