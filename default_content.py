'''
This file contains a function to get the default content for a canvas based on the block type
'''

import json # used to convert json to string before saving to db
#from .auto_pipelines.sklearn_classification import ClassificationPipeline
#from .auto_pipelines.sklearn_regression import RegressionPipeline
from .auto_pipelines.sklearn_pypeline import SklearnPipeline


def default_content(block_type: int) -> str | None:
    """Get the default content for a block based on the block type"""
    if block_type == 5: # Pypeline Block
        config = {
            'dataset': None,
            'target_column': None,
            'model_type': None,
            'cross_validation': 5,
            'selected_models': [],
            'completed_models': []
            #'pipeline':SklearnPipeline().get_settings()
        }
        return json.dumps(config)
    else: 
        return "" 