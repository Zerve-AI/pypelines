from ..model_base import PYODModelBase, PYODModelComparisonBase

iforest_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_estimators', 'min': 100, 'max': 500, 'step': 100},
    ],
    'categorical': [
    ]

}

class IForestAnomalyDetection(PYODModelBase):
    def __init__(self):
        model_string = 'IForest()'
        imports = '''from pyod.models.iforest import IForest\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('IForest', model_string, iforest_hyperparams, imports,model_type)

class IForestAnomalyDetectionComparison(PYODModelComparisonBase):
    def __init__(self):
        model_string = 'IForest()'
        imports = '''from pyod.models.iforest import IForest\nimport matplotlib.pyplot as plt'''
        model_type ='Anomaly Detection'
        super().__init__('IForest', model_string, iforest_hyperparams, imports,model_type)