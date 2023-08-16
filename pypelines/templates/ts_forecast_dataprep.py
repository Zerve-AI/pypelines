from .template_base import AutoPipelineBaseTemplate


required_imports = """
import pandas as pd
import numpy as np
"""

template = """
target_col='{{target_column}}'
date_col = '{{date_column}}'

{% if exo == "True" %}
features = list({{dataset}}.columns.drop(target_col))
y = {{dataset}}[[date_col,target_col]]
y_train_preprocessed = y
y_train_preprocessed[date_col] = pd.to_datetime(y_train_preprocessed[date_col],format = "{{date_format}}")
y_train_preprocessed = y_train_preprocessed.set_index(date_col)
y_train_preprocessed.index = y_train_preprocessed.index.to_period(freq = "{{frequency}}")
X = {{dataset}}[features]
x_train_preprocessed = X
x_train_preprocessed[date_col] = pd.to_datetime(x_train_preprocessed[date_col],format = "{{date_format}}")
x_train_preprocessed = x_train_preprocessed.set_index(date_col)
x_train_preprocessed.index = x_train_preprocessed.index.to_period(freq = "{{frequency}}")
{% elif exo == "False" %}
y = {{dataset}}[[date_col,target_col]]
y_train_preprocessed = y
y_train_preprocessed[date_col] = pd.to_datetime(y_train_preprocessed[date_col],format = "{{date_format}}")
y_train_preprocessed = y_train_preprocessed.set_index(date_col)
y_train_preprocessed.index = y_train_preprocessed.index.to_period(freq = "{{frequency}}")
{% endif %}
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
