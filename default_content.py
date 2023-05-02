'''
This file contains a function to get the default content for a canvas based on the block type
'''

import json # used to convert json to string before saving to db
#from .auto_pipelines.sklearn_classification import ClassificationPipeline
#from .auto_pipelines.sklearn_regression import RegressionPipeline
from pypelines.sklearn_pypeline import SklearnPipeline


def default_content(block_type: int):
    """Get the default content for a block based on the block type"""
    if block_type == 5: # Pypeline Block
        config = {
            'dataset': 'train.csv',
            'target_column': 'target',
            'model_type': 'regression',
            'cross_validation': 5,
            'selected_models': ['Bayesian Ridge Regression'],
            'completed_models': [],
            'classification': SklearnPipeline().get_settings_classification(),
            'regression': SklearnPipeline().get_settings_regression()
        }
        return json.dumps(config)
    else: 
        return "" 