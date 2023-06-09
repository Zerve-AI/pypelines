from ..model_base import PYODModelBase, PYODModelComparisonBase

deepsvdd_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'epochs', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'batch_size', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'dropout_rate', 'min': 0.01, 'max': 1, 'step': 0.2},
    ],
    'categorical': [
        {'search': True, 'name': 'hidden_activation', 'selected': ['relu'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
        {'search': True, 'name': 'output_activation', 'selected': ['sigmoid'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
    ]
}

class DeepSVDDAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'DeepSVDD()'
        imports = '''from pyod.models.deep_svdd import DeepSVDD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('DeepSVDD', model_string, deepsvdd_hyperparams, imports,model_type)

class DeepSVDDAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'DeepSVDD()'
        imports = '''from pyod.models.deep_svdd import DeepSVDD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('DeepSVDD', model_string, deepsvdd_hyperparams, imports,model_type)