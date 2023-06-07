from ..model_base import PYODModelBase, PYODModelComparisonBase

anogan_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'epochs', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'batch_size', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'dropout_rate', 'min': 0.01, 'max': 1, 'step': 0.2},
    ],
    'categorical': [
        {'search': True, 'name': 'output_activation', 'selected': ['relu'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
        {'search': True, 'name': 'activation_hidden', 'selected': ['tanh'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
    ]
}


class AnoGANAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'AnoGAN()'
        imports = '''from pyod.models.anogan import AnoGAN\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('AnoGAN', model_string, anogan_hyperparams, imports,model_type)

class AnoGANAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'AnoGAN()'
        imports = '''from pyod.models.anogan import AnoGAN\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('AnoGAN', model_string, anogan_hyperparams, imports,model_type)