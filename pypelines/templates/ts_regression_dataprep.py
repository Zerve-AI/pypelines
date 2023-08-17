from .template_base import AutoPipelineBaseTemplate


required_imports = """
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
"""

template = """

# target dataframe: {{dataset}}
target = "{{target_column}}"
features = list({{dataset}}.columns.drop("{{target_column}}"))

# train test split
X_train = {{dataset}}[features]
y_train = {{dataset}}[target]

X_test = {{test_dataset}}[features]
y_test = {{test_dataset}}[target]

model_comparison_list = []
"""



class TSRegressionTemplate(AutoPipelineBaseTemplate):
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
                         requirements=['scikit-learn', 'pandas', 'numpy'],
                         required_imports=required_imports)
    
    def template(self):
        """
        The template function is used to create a new template.
            
        
        :param self: Represent the instance of the class
        :return: The template file
        """
        return 
