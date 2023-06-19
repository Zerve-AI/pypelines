from .template_base import AutoPipelineBaseTemplate


required_imports = """
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import sktime
"""

template = """
features = list({{dataset}}.columns)
feature_df = {{dataset}}[features]

x_train = {{dataset}}[features]

x_train_preprocessed = x_train

model_comparison_list = []
"""



class TSTemplate(AutoPipelineBaseTemplate):
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the template, requirements and required imports for this particular 
        class. The template will be used to generate a Python script that can be run on 
        the command line or in a Jupyter notebook.
        
        :param self: Represent the instance of the class
        :return: A class object
        :doc-author: Trelent
        """
        super().__init__(
                        template=template,
                         requirements=['scikit-learn', 'pyod', 'pandas', 'numpy','sktime'],
                         required_imports=required_imports)
    
    def template(self):
        """
        The template function is used to create a new template.
            
        
        :param self: Represent the instance of the class
        :return: The template file
        """
        return 
