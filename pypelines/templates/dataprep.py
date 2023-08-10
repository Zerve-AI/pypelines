from .template_base import AutoPipelineBaseTemplate

required_imports = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from feature_engine.encoding import CountFrequencyEncoder
"""

template = """
# target dataframe: {{dataset}}
target = "{{target_column}}"
features = list({{dataset}}.columns.drop("{{target_column}}"))
feature_df = {{dataset}}[features]

{% if outlier_method != None %}
# Handling Outliers
try:
    {% if outlier_method == 'ArbitraryCapper' %}
    out = ArbitraryOutlierCapper(max_capping_dict=None, min_capping_dict=None, missing_values='ignore')
    {{dataset}} = out.fit_transform({{dataset}})

    {% elif outlier_method == 'Outlier Trimmer' %}
    out = OutlierTrimmer(capping_method='gaussian', tail='right', fold=3, variables=None, missing_values='ignore')
    {{dataset}} = out.fit_transform({{dataset}})

    {% elif outlier_method == 'Winsorizer' %}
    out = Winsorizer(capping_method='gaussian', tail='right', fold=3, add_indicators=False, variables=None, missing_values='ignore')
    {{dataset}} = out.fit_transform({{dataset}})
    {% endif %}
except Exception as e:
    print("Error in outlier:", str(e))
{% endif %} 

{% if numerical_imputation != None or categorical_imputation != None %}
# Missing Value Imputation

# Identifying the missing columns and selecting only columns with less than 10% missing values
edited_missing_columns = feature_df.columns[feature_df.isnull().mean() <= 0.1].tolist()

if len(edited_missing_columns) != 0:
    int_lst = {{dataset}}[edited_missing_columns].select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_lst = {{dataset}}[edited_missing_columns].select_dtypes(include=['category','object']).columns.tolist()
    try:
        if len(int_lst) > 0:
            {% if numerical_imputation == "MeanMedianImputer" %}
            imputer = MeanMedianImputer(imputation_method='median', variables=int_lst)
            {{dataset}}_num = imputer.fit_transform({{dataset}}[int_lst])

            {% elif numerical_imputation == "CategoricalImputer" %}
            imputer = CategoricalImputer(imputation_method='missing',variables=int_lst)
            {{dataset}}_num  = imputer.fit_transform({{dataset}}[int_lst])

            {% elif numerical_imputation == "AddMissingIndicator" %}
            imputer = AddMissingIndicator(missing_only=True,variables=int_lst)
            {{dataset}}_num= imputer.fit_transform({{dataset}}[int_lst])

            {% elif numerical_imputation == "ArbitraryNumberImputer" %}
            imputer = ArbitraryNumberImputer(arbitrary_number=-999,variables=int_lst)
            {{dataset}}_num = imputer.fit_transform({{dataset}}[int_lst])

            {% elif numerical_imputation == "EndTailImputer" %}
            imputer = EndTailImputer(imputation_method='gaussian',tail='right',variables=int_lst)
            {{dataset}}_num = imputer.fit_transform({{dataset}}[int_lst])

            {% elif numerical_imputation == "RandomSampleImputer" %}
            imputer = RandomSampleImputer(variables=int_lst)
            {{dataset}}_num = imputer.fit_transform({{dataset}}[int_lst])
            {% endif %}
    except Exception as e:
        print("Error in integer imputation:", str(e))

    try:
        if len(cat_lst) > 0:
            {% if categorical_imputation == "CategoricalImputer" %}
            imputer = CategoricalImputer(imputation_method='missing',variables=cat_lst)
            {{dataset}}_cat = imputer.fit_transform({{dataset}}[cat_lst])

            {% elif categorical_imputation == "AddMissingIndicator" %}
            imputer = AddMissingIndicator(missing_only=True,variables=cat_lst)
            {{dataset}}_cat = imputer.fit_transform({{dataset}}[cat_lst])

            {% elif categorical_imputation == "RandomSampleImputer" %}
            imputer = RandomSampleImputer(variables=cat_lst)
            {{dataset}}_cat= imputer.fit_transform({{dataset}}[cat_lst])
            {% endif %}
    except Exception as e:
        print("Error in integer imputation:", str(e))
else:
    pass
        
feature_df = pd.concat([{{dataset}}_num,{{dataset}}_cat],axis=1)
{{dataset}} =  pd.concat([feature_df,{{dataset}}["{{target_column}}"]],axis=1)
{% endif %}


{% if encoding != None %}
# Encoding Categorical Variables
try:
    {% if encoding == "MeanEncoder" %}
    encode = CountFrequencyEncoder(encoding_method='count', variables=None, missing_values='raise', ignore_format=False, unseen='ignore')
    x = {{dataset}}.drop(columns='{{target}}', axis=1)
    y = {{dataset}}['{{target}}']
    {{dataset}} = encode.fit_transform(x, y)

    {% elif encoding == "WoEEncoder" %}
    x = {{dataset}}.drop(columns='{{target}}', axis=1)
    y = {{dataset}}['{{target}}']
    {{dataset}} = encode.fit_transform(x, y)

    {% elif encoding == "OrdinalEncoder" %}
    encode = OrdinalEncoder(encoding_method='ordered', variables=None, missing_values='raise', ignore_format=False, unseen='ignore')
    x = {{dataset}}.drop(columns='{{target}}', axis=1)
    y = {{dataset}}['{{target}}']
    {{dataset}} = encode.fit_transform(x, y)

    {% elif encoding == "DecisionTreeEncoder" %}
    encode = DecisionTreeEncoder(encoding_method='arbitrary', cv=3, scoring='neg_mean_squared_error', param_grid=None, regression=True, random_state=None, variables=None, ignore_format=False)
    x = {{dataset}}.drop(columns='{{target}}', axis=1)
    y = {{dataset}}['{{target}}']
    {{dataset}} = encode.fit_transform(x, y)

    {% elif encoding == "OneHotEncoder" %}
    encode = OneHotEncoder(top_categories=None, drop_last=False, drop_last_binary=False, variables=None, ignore_format=False)
    {{dataset}} = encode.fit_transform({{dataset}})

    {% elif encoding == "StringSimilarityEncoder" %}
    encode = StringSimilarityEncoder(top_categories=None, keywords=None, missing_values='impute', variables=None, ignore_format=False)
    {{dataset}} = encode.fit_transform({{dataset}})

    {% elif encoding == "CountFrequencyEncode" %}
    encode = CountFrequencyEncoder(encoding_method='count', variables=None, missing_values='raise', ignore_format=False, unseen='ignore')
    {{dataset}} = encode.fit_transform({{dataset}})

    {% elif encoding == "RareLabelEncoder" %}
    encode = RareLabelEncoder(tol=0.05, n_categories=10, max_n_categories=None, replace_with='Rare', variables=None, missing_values='raise', ignore_format=False)
    {{dataset}} = encode.fit_transform({{dataset}})
    {% endif %}
except Exception as e:
    print("Error in integer encoding:", str(e))
{% endif %}

{% if datetime_method != None %}
# Datetime Features
try:
    {% if datetime_method == "DatetimeFeatures" %}
    dt = DatetimeFeatures(variables=None, features_to_extract=None, drop_original=True, missing_values='raise', dayfirst=False, yearfirst=False, utc=None)
    dtf = dt(features_to_extract = ["year", "month", "day_of_month"])
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    y = {{dataset}}["{{target_column}}"]
    x = dtf.fit_transform(x)
    {{dataset}} = pd.concat([x,y])


    {% elif datetime_method == "DatetimeSubtraction" %}
    dt = DatetimeSubtraction(variables, reference, new_variables_names=None, output_unit='D', missing_values='ignore', drop_original=False, dayfirst=False, yearfirst=False, utc=None)    
    dtf = dt(variables=["{{target_date1_column}}"], reference=["{{target_date2_column}}"])
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    y = {{dataset}}["{{target_column}}"]
    x = dtf.fit_transform(x)
    {{dataset}} = pd.concat([x,y])

    {% endif %}
except Exception as e:
    print("Error in integer datetime:", str(e))
{% endif %}

{% if discretisation_method != None %}
# Discretisation
try:
    {% if discretisation_method == "DecisionTreeDiscretiser" %}
    discret = DecisionTreeDiscretiser(variables=None, cv=3, scoring='neg_mean_squared_error', param_grid=None, regression=True, random_state=None)
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    y = {{dataset}}["{{target_column}}"]
    x = discret.fit_transform(x, y)

    {% elif discretisation_method == "ArbitraryDiscretiser" %}
    discret = ArbitraryDiscretiser(return_object=False, return_boundaries=False, precision=3, errors='ignore')
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    x = discret.fit_transform(x)

    {% elif discretisation_method == "EqualFrequencyDiscretiser" %}
    discret = EqualFrequencyDiscretiser(variables=None, q=10, return_object=False, return_boundaries=False, precision=3)
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    x = discret.fit_transform(x)

    {% elif discretisation_method == "EqualWidthDiscretiser" %}
    discret = EqualWidthDiscretiser(variables=None, bins=10, return_object=False, return_boundaries=False, precision=3)
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    x = discret.fit_transform(x)

    {% elif discretisation_method == "GeometricWidthDiscretiser" %}
    discret = GeometricWidthDiscretiser(variables=None, bins=10, return_object=False, return_boundaries=False, precision=7)
    x = {{dataset}}.drop("{{target_column}}", axis=1)
    x = discret.fit_transform(x)
    {% endif %}
except Exception as e:
    print("Error in integer encoding:", str(e))
{% endif %}
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
                         required_imports=required_imports
                         )
    
    def template(self):
        """
        The template function is used to create a new template.
            
        
        :param self: Represent the instance of the class
        :return: The template file
        """
        return 