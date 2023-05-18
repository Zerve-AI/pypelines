from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

titanic = pd.read_csv("pypelines/datasets/classification/titanic.csv")

# target dataframe: titanic
target = "Survived"
features = list(titanic.columns.drop("Survived"))
feature_df = titanic[features]

# get numerical and categorical columns
bool_cols = feature_df.select_dtypes(include=['bool']).columns.tolist()
titanic[bool_cols] = feature_df[bool_cols].astype(int)
numerical_cols = feature_df.select_dtypes(include=['int', 'float']).columns.tolist()
categorical_cols = feature_df.select_dtypes(include=['object']).columns.tolist()
text_cols = feature_df.select_dtypes(include=['string']).columns.tolist()


sample_size = np.min([10000, titanic.shape[0]])
unique_theshold = np.min([100, sample_size/10])

# check categorical columns for high cardinality and make it text column
for col in categorical_cols:
    if titanic[col].sample(sample_size).nunique() > unique_theshold:
        text_cols.append(col)
        categorical_cols.remove(col)
        

# check text columns for low cardinality and make it categorical columns
for col in text_cols:
    if titanic[col].sample(sample_size).nunique() < unique_theshold:
        categorical_cols.append(col)
        text_cols.remove(col)

print(numerical_cols)
print(categorical_cols)
print(text_cols)

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
        transformers=[('num', numeric_transformer , numerical_cols),
        ('cat', categorical_transformer, categorical_cols),
        *[(f'text_{t_col}', text_transformer, t_col) for t_col in text_cols]]
)

# train test split
X = titanic[features]
y = titanic[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

##### End of Data Processing Pipeline #####


##### Model Pipeline for Logistic Regression #####

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc
import matplotlib.pyplot as plt
log_reg_param_grid = {
"log_reg__C": np.arange(0.1, 1.0, 0.1),
}


# Create the pipeline
log_reg_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('log_reg', LogisticRegression())
])

# Create the grid search
log_reg_grid_search = GridSearchCV(estimator=log_reg_pipe, param_grid=log_reg_param_grid, cv=5, scoring=make_scorer(accuracy_score), verbose=1)
log_reg_grid_search.fit(X_train, y_train)

# Get the best hyperparameters
log_reg_best_estimator = log_reg_grid_search.best_estimator_

# Store results as a dataframe  
log_reg_search_results = pd.DataFrame(log_reg_grid_search.cv_results_)

# Model metrics

# Generate Predictions
log_reg_predictions = pd.DataFrame(log_reg_best_estimator.predict(X_test))
log_reg_predictions_prob = log_reg_best_estimator.predict_proba(X_test)
log_reg_predictions_prob_df = pd.DataFrame()
log_reg_predictions_prob_df[log_reg_grid_search.classes_[0]] = log_reg_predictions_prob[:,0]
log_reg_predictions_prob_df[log_reg_grid_search.classes_[1]] = log_reg_predictions_prob[:,1] 

# Generate Model Metrics
log_reg_accuracy = accuracy_score(y_test, log_reg_predictions.iloc[:,0])
log_reg_f1_score = f1_score(y_test, log_reg_predictions.iloc[:,0])
log_reg_precision = precision_score(y_test, log_reg_predictions.iloc[:,0])
log_reg_recall = recall_score(y_test, log_reg_predictions.iloc[:,0])
log_reg_roc_auc_score = roc_auc_score(y_test, log_reg_predictions_prob_df[log_reg_grid_search.classes_[1]])
log_reg_performance_metrics = [['log_reg','accuracy',log_reg_accuracy], 
                                  ['log_reg','f1_score',log_reg_f1_score],
                                  ['log_reg','precision', log_reg_precision],
                                  ['log_reg','recall', log_reg_recall],
                                  ['log_reg','roc_auc_score', log_reg_roc_auc_score]]
log_reg_performance_metrics = pd.DataFrame(log_reg_performance_metrics, columns=['model','metric', 'value'])
fpr, tpr, thresholds = roc_curve(y_test, log_reg_predictions_prob_df[log_reg_grid_search.classes_[1]])
roc_auc = auc(fpr, tpr)

# Generate ROC Curve plot
log_reg_roc_auc_plot, log_reg_roc_auc_plot_ax = plt.subplots()
log_reg_roc_auc_plot_ax.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.4f})')
log_reg_roc_auc_plot_ax.plot([0, 1], [0, 1], 'r--', label='Random guess')
# Set axis labels and title
log_reg_roc_auc_plot_ax.set_xlabel('False Positive Rate')
log_reg_roc_auc_plot_ax.set_ylabel('True Positive Rate')
log_reg_roc_auc_plot_ax.set_title('ROC Curve')
# Add legend
log_reg_roc_auc_plot_ax.legend()

# Generate Decile Lift Chart
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

def plot_lift(y_real, y_proba, ax = None, color = 'b', title = 'Lift Curve', xlabel = 'Proportion', ylabel = 'Lift'):
    # Prepare the data
    aux_df = pd.DataFrame()
    aux_df['y_real'] = y_real
    aux_df['y_proba'] = y_proba[:,1]
    # Sort by predicted probability
    aux_df = aux_df.sort_values('y_proba', ascending = False)
    # Find the total positive ratio of the whole dataset
    total_positive_ratio = sum(aux_df['y_real'] == 1) / aux_df.shape[0]
    # For each line of data, get the ratio of positives of the given subset and calculate the lift
    lift_values = []
    for i in aux_df.index:
        threshold = aux_df.loc[i]['y_proba']
        subset = aux_df[aux_df['y_proba'] >= threshold]
        subset_positive_ratio = sum(subset['y_real'] == 1) / subset.shape[0]
        lift = subset_positive_ratio / total_positive_ratio
        lift_values.append(lift)
    # Plot the lift curve
    if ax == None:
        ax = plt.axes()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    sns.lineplot(x = [x/len(lift_values) for x in range(len(lift_values))], y = lift_values, ax = ax, color = color)
    ax.axhline(1, color = 'gray', linestyle = 'dashed', linewidth = 3)


plot_lift(y_real=y_test,y_proba=log_reg_predictions_prob)


print(log_reg_performance_metrics)
plt.show(block=False)


##### Model Metrics Logistic Regression #####

print(log_reg_performance_metrics)
plt.show(block=False)

##### End of Model Pipeline for Logistic Regression #####