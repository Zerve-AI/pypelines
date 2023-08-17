from .template_base import AutoPipelineBaseTemplate


required_imports = """
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
"""

template = """

features = list({{dataset}}.columns)

# train test split
X_train = {{dataset}}[features]

model_comparison_list = []
"""



class TSClusteringTemplate(AutoPipelineBaseTemplate):
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
