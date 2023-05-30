from ..model_base import PYODModelBase, PYODModelComparisonBase

alad_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'epochs', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'batch_size', 'min': 100, 'max': 1000, 'step': 100},
        {'search': True, 'name': 'dropout_rate', 'min': 0.01, 'max': 1, 'step': 0.2},
    ],
    'categorical': [
        {'search': True, 'name': 'activation_hidden_gen', 'selected': ['relu'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
        {'search': True, 'name': 'activation_hidden_disc', 'selected': ['relu'], 'values': ['relu', 'sigmoid','softmax','softplus','softsign','tanh','selu','elu','exponential']},
    ]
}


class ALADAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'ALAD()'
        imports = '''from pyod.models.alad import ALAD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ALAD', model_string, alad_hyperparams, imports,model_type)

class ALADAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'ALAD()'
        imports = '''from pyod.models.alad import ALAD\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('ALAD', model_string, alad_hyperparams, imports,model_type)