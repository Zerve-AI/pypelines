
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error


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


# target dataframe: housing
housing = pd.read_csv(r"C:\zerve\pypelines\pypelines\datasets\regression\housing.csv")
target = "['median_income']"
features = list(housing.columns.drop("['median_income']"))
feature_df = housing[features]

# get numerical and categorical columns
bool_cols = feature_df.select_dtypes(include=['bool']).columns.tolist()
housing[bool_cols] = feature_df[bool_cols].astype(int)
numerical_cols = feature_df.select_dtypes(include=['int', 'float']).columns.tolist()
categorical_cols = feature_df.select_dtypes(include=['object']).columns.tolist()
text_cols = feature_df.select_dtypes(include=['string']).columns.tolist()
# check categorical columns for high cardinality

sample_size = np.min([10000, housing.shape[0]])
unique_theshold = np.min([100, sample_size/10])

# check categorical columns for high cardinality
for col in categorical_cols:
    if housing[col].sample(sample_size).nunique() > unique_theshold:
        categorical_cols.remove(col)

# check text columns for low cardinality
for col in text_cols:
    if housing[col].sample(sample_size).nunique() < unique_theshold:
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
        ("imputer", SimpleImputer(strategy="most_frequent")), 
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
X = housing[features]
y = housing[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##### End of Data Processing Pipeline #####



##### Model Pipeline for RANSAC Regression #####

from sklearn.linear_model import RANSACRegressor 
from sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score
import plotly.express as px
import plotly.graph_objects as go
ransac_regression_param_grid = {
"ransac_regression__alpha": np.arange(10, 100, 10),
"ransac_regression__max_trials": np.arange(10, 100, 10),
}


# Create the pipeline
ransac_regression_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('ransac_regression', RANSACRegressor())
])

# Create the grid search
ransac_regression_grid_search = GridSearchCV(estimator=ransac_regression_pipe, param_grid=ransac_regression_param_grid, cv=5, scoring=make_scorer(mean_squared_error), verbose=1)
ransac_regression_grid_search.fit(X_train, y_train)

# Get the best hyperparameters
ransac_regression_best_estimator = ransac_regression_grid_search.best_estimator_

# Store results as a dataframe  
ransac_regression_search_results = pd.DataFrame(ransac_regression_grid_search.cv_results_)

# Model metrics

ransac_regression_predictions = pd.DataFrame(ransac_regression_best_estimator.predict(X_test))
ransac_regression_r2_score = r2_score(y_test, ransac_regression_predictions.iloc[:,0])
ransac_regression_mean_squared_error = mean_squared_error(y_test, ransac_regression_predictions.iloc[:,0])
ransac_regression_explained_variance_score = explained_variance_score(y_test, ransac_regression_predictions.iloc[:,0])
ransac_regression_performance_metrics = [['ransac_regression','r2_score', ransac_regression_r2_score], 
                                  ['ransac_regression','mean_squared_error',ransac_regression_mean_squared_error],
                                  ['ransac_regression','explained_variance_score', ransac_regression_explained_variance_score]]
ransac_regression_performance_metrics = pd.DataFrame(ransac_regression_performance_metrics, columns=['model','metric', 'value'])
ransac_regression_actual_predicted_plot = px.scatter(x=y_test, y=ransac_regression_predictions.iloc[:,0])
ransac_regression_actual_predicted_plot.add_shape(type="line", line=dict(dash='dash'),x0=y.min(), y0=y.min(), x1=y.max(), y1=y.max())
ransac_regression_actual_predicted_plot.update_layout(title="Actual vs Predicted",xaxis_title="Actual",yaxis_title="Predicted")
del df, target, features, feature_df, bool_cols, numerical_cols, categorical_cols, text_cols, col, numeric_transformer, categorical_transformer,text_transformer, preprocessor,X, X_train, X_test, y, y_train, y_test,mean_squared_error,make_scorer,r2_score,explained_variance_score


##### Model Metrics RANSAC Regression #####

ransac_regression_performance_metrics
ransac_regression_actual_predicted_plot.show()

##### End of Model Pipeline for RANSAC Regression #####
