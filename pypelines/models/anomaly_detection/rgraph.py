from ..model_base import PYODModelBase, PYODModelComparisonBase

rgraph_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'maxiter_lasso', 'min': 100, 'max': 1000, 'step': 1000},
        {'search': True, 'name': 'transition_steps', 'min': 10, 'max': 20, 'step': 15}
    ],
    'categorical': [
        {'search': True, 'name': 'verbose', 'selected': [1], 'values': [0,1,2]},
        {'search': False, 'name': 'fit_intercept_LR', 'selected': [False], 'values': [True,False]},
        {'search': False, 'name': 'active_support', 'selected': [True], 'values': [True,False]},
        
    ]
}

class RGraphAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'RGraph()'
        imports = '''from pyod.models.rgraph import RGraph\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('RGraph', model_string, rgraph_hyperparams, imports,model_type)

class RGraphAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'RGraph()'
        imports = '''from pyod.models.rgraph import RGraph\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('RGraph', model_string, rgraph_hyperparams, imports,model_type)