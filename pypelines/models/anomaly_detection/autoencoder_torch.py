from ..model_base import PYODModelBase, PYODModelComparisonBase

auto_encoder_torch_hyperparams = {
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


class AutoEncoderTorchAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'AutoEncoder()'
        imports = '''from pyod.models.auto_encoder_torch import AutoEncoder\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('AutoEncoder', model_string, auto_encoder_torch_hyperparams, imports,model_type)

class AutoEncoderTorchAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'AutoEncoder()'
        imports = '''from pyod.models.auto_encoder_torch import AutoEncoder\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('AutoEncoder', model_string, auto_encoder_torch_hyperparams, imports,model_type)