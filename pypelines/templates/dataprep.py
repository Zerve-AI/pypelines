from ..templates.template_base import AutoPipelineBaseTemplate
from feature_engine.imputation import MeanMedianImputer, CategoricalImputer, ArbitraryNumberImputer, EndTailImputer, RandomSampleImputer, AddMissingIndicator, DropMissingData


imputators = [
    MeanMedianImputer(imputation_method='median', variables=None),
    ArbitraryNumberImputer(arbitrary_number=999, variables=None, imputer_dict=None),
    EndTailImputer(imputation_method='gaussian', tail='right', fold=3, variables=None),
    CategoricalImputer(imputation_method='missing', fill_value='Missing', variables=None, return_object=False, ignore_format=False),
    RandomSampleImputer(variables=None, random_state=None, seed='general', seeding_method='add'),
    AddMissingIndicator(missing_only=True, variables=None),
    DropMissingData(missing_only=True, threshold=None, variables=None)
]


required_imports = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from feature_engine.imputation import MeanMedianImputer, CategoricalImputer, ArbitraryNumberImputer, EndTailImputer, RandomSampleImputer, AddMissingIndicator, DropMissingData
"""

template = """
# HANDLING OUTLIERS
{{dataset}} = out.fit_transform({{dataset}})

# MISSING VALUE IMPUTATION

# Identifying the missing columns and selecting only columns with less than 10% missing values
edited_missing_columns = {{dataset}}.columns[{{dataset}}.isnull().mean() <= 0.1].tolist()

if len(edited_missing_columns) != 0:
    int_lst = {{dataset}}[edited_missing_columns].select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_lst = {{dataset}}[edited_missing_columns].select_dtypes(include=['object']).columns.tolist()

    try:
        if len(int_lst) > 0:
            imputer = MeanMedianImputer(imputation_method='median', variables=int_lst)
            {{dataset}}[int_lst] = imputer.fit_transform({{dataset}}[int_lst])
    except Exception as e:
        print("Error in integer imputation:", str(e))

    try:
        if len(cat_lst) > 0:
            imputer = CategoricalImputer(variables=cat_lst)
            {{dataset}}[cat_lst] = imputer.fit_transform({{dataset}}[cat_lst])
    except Exception as e:
        print("Error in categorical imputation:", str(e))

{{dataset}} = {{dataset}}.dropna(axis=1)

# ENCODING CATEGORICAL VARIABLES
try:
    if {{encoding_models}}[0] not in ["MeanEncoder", "WoEEncoder", "OrdinalEncoder", "DecisionTreeEncoder"]:
        {{dataset}} = encode.fit_transform({{dataset}})
    else:
        x = {{dataset}}.drop(columns='{{target}}', axis=1)
        y = {{dataset}}['{{target}}']
        {{dataset}} = encode.fit_transform(x, y)
except Exception as e:
    print("Error in encoding:", str(e))

"""



class DataPrepTemplate(AutoPipelineBaseTemplate):
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
                         requirements=['scikit-learn', 'pandas', 'numpy', 'matplotlib', 'feature_engine'],
                         required_imports=required_imports)
    
    def template(self):
        """
        The template function is used to create a new template.
            
        
        :param self: Represent the instance of the class
        :return: The template file
        """
        return 
