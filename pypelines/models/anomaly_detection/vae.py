from ..model_base import PYODModelBase, PYODModelComparisonBase

vae_hyperparams = {
    'numerical': [
        {'search': False, 'name': 'contamination', 'min': 0.1, 'max': 0.5, 'step': 0.05},
        {'search': False, 'name': 'epochs', 'min': 10, 'max': 100, 'step': 10},
        {'search': False, 'name': 'batch_size', 'min': 8, 'max': 32, 'step': 2}
    ]
}

class VAEAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'VAE()'
        imports = '''from pyod.models.vae import VAE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('VAE', model_string, vae_hyperparams, imports,model_type)

class VAEAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'VAE()'
        imports = '''from pyod.models.vae import VAE\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('VAE', model_string, vae_hyperparams, imports,model_type)