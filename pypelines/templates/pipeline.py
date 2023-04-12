from .template_base import AutoPipelineBaseTemplate


required_imports = """
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import plotly.express as px
import plotly.graph_objects as go
"""

template = """

# target dataframe: {{dataset}}
target = "{{target_column}}"
features = list({{dataset}}.columns.drop("{{target_column}}"))
feature_df = {{dataset}}[features]

# get numerical and categorical columns
bool_cols = feature_df.select_dtypes(include=['bool']).columns.tolist()
{{dataset}}[bool_cols] = feature_df[bool_cols].astype(int)
numerical_cols = feature_df.select_dtypes(include=['int', 'float']).columns.tolist()
categorical_cols = feature_df.select_dtypes(include=['object']).columns.tolist()
text_cols = feature_df.select_dtypes(include=['string']).columns.tolist()
# check categorical columns for high cardinality

sample_size = np.min([10000, {{dataset}}.shape[0]])
unique_theshold = np.min([100, sample_size/10])

# check categorical columns for high cardinality
for col in categorical_cols:
    if {{dataset}}[col].sample(sample_size).nunique() > unique_theshold:
        categorical_cols.remove(col)

# check text columns for low cardinality
for col in text_cols:
    if {{dataset}}[col].sample(sample_size).nunique() < unique_theshold:
        categorical_cols.append(col)
        text_cols.remove(col)

# define numeric transformer steps
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")), 
        ("scaler", StandardScaler())]
)

# define categorical transformer steps
categorical_transformer = Pipeline(
    steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)

# define text transformer steps
text_transformer = Pipeline(
    steps=[
        ('text', TfidfVectorizer())
    ]
)

# create the preprocessing pipelines for both numeric and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer , numerical_cols),
        ('cat', categorical_transformer, categorical_cols),
        ('text', text_transformer, text_cols),
    ]
)

# train test split
X = {{dataset}}[features]
y = {{dataset}}[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
"""



class PipelineTemplate(AutoPipelineBaseTemplate):
    def __init__(self):
        super().__init__(
                        template=template,
                         requirements=['scikit-learn', 'pandas', 'numpy'],
                         required_imports=required_imports)
    
    def template(self):
        return 
