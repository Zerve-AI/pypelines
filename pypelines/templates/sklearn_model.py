from .template_base import AutoPipelineBaseTemplate


template = '''
{{imports}}
{{prefix}}_param_grid = {{hyperparams}}

# Create the pipeline
{{prefix}}_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('{{prefix}}', {{model}})
])

# Create the grid search
{{prefix}}_grid_search = GridSearchCV(estimator={{prefix}}_pipe, param_grid={{prefix}}_param_grid, cv={{cross_validation}}, scoring=make_scorer({{metric}}), verbose=1)
{{prefix}}_grid_search.fit(X_train, y_train)

# Get the best hyperparameters
{{prefix}}_best_estimator = {{prefix}}_grid_search.best_estimator_

# Store results as a dataframe  
{{prefix}}_search_results = pd.DataFrame({{prefix}}_grid_search.cv_results_)

# Model metrics
{% if model_type == "Regression" %}
{{prefix}}_predictions = pd.DataFrame({{prefix}}_best_estimator.predict(X_test))
{{prefix}}_r2_score = r2_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_mean_squared_error = mean_squared_error(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_explained_variance_score = explained_variance_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_performance_metrics = [['{{prefix}}','r2_score', {{prefix}}_r2_score], 
                                  ['{{prefix}}','mean_squared_error',{{prefix}}_mean_squared_error],
                                  ['{{prefix}}','explained_variance_score', {{prefix}}_explained_variance_score]]
{{prefix}}_performance_metrics = pd.DataFrame({{prefix}}_performance_metrics, columns=['model','metric', 'value'])


{{prefix}}_actual_predicted_plot, {{prefix}}_actual_predicted_plot_ax = plt.subplots()
{{prefix}}_actual_predicted_plot = {{prefix}}_actual_predicted_plot_ax.scatter(x=y_test, y={{prefix}}_predictions.iloc[:,0], alpha=0.5)
# Add diagonal line
{{prefix}}_actual_predicted_plot_ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', alpha=0.5)
# Set axis labels and title
{{prefix}}_actual_predicted_plot_ax.set_xlabel('Actual')
{{prefix}}_actual_predicted_plot_ax.set_ylabel('Predicted')
{{prefix}}_actual_predicted_plot_ax.set_title('Actual vs. Predicted')

{% elif model_type == "Classification" %}
{{prefix}}_predictions = pd.DataFrame({{prefix}}_best_estimator.predict(X_test))
{{prefix}}_predictions_prob = {{prefix}}_best_estimator.predict_proba(X_test)
{{prefix}}_predictions_prob_df = pd.DataFrame()
{{prefix}}_predictions_prob_df[{{prefix}}_grid_search.classes_[0]] = {{prefix}}_predictions_prob[:,0]
{{prefix}}_predictions_prob_df[{{prefix}}_grid_search.classes_[1]] = {{prefix}}_predictions_prob[:,1] 
{{prefix}}_accuracy = accuracy_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_f1_score = f1_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_precision = precision_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_recall = recall_score(y_test, {{prefix}}_predictions.iloc[:,0])
{{prefix}}_roc_auc_score = roc_auc_score(y_test, {{prefix}}_predictions_prob_df[{{prefix}}_grid_search.classes_[1]])
{{prefix}}_performance_metrics = [['{{prefix}}','accuracy',{{prefix}}_accuracy], 
                                  ['{{prefix}}','f1_score',{{prefix}}_f1_score],
                                  ['{{prefix}}','precision', {{prefix}}_precision],
                                  ['{{prefix}}','recall', {{prefix}}_recall],
                                  ['{{prefix}}','roc_auc_score', {{prefix}}_roc_auc_score]]
{{prefix}}_performance_metrics = pd.DataFrame({{prefix}}_performance_metrics, columns=['model','metric', 'value'])

fpr, tpr, thresholds = roc_curve(y_test, {{prefix}}_predictions_prob_df[{{prefix}}_grid_search.classes_[1]])
roc_auc = auc(fpr, tpr)
# Create plot
{{prefix}}_roc_auc_plot, {{prefix}}_roc_auc_plot_ax = plt.subplots()
{{prefix}}_roc_auc_plot_ax.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.4f})')
{{prefix}}_roc_auc_plot_ax.plot([0, 1], [0, 1], 'r--', label='Random guess')

# Set axis labels and title
{{prefix}}_roc_auc_plot_ax.set_xlabel('False Positive Rate')
{{prefix}}_roc_auc_plot_ax.set_ylabel('True Positive Rate')
{{prefix}}_roc_auc_plot_ax.set_title('ROC Curve')

# Add legend
{{prefix}}_roc_auc_plot_ax.legend()
plt.show()
{% endif %}


'''

class SkLearnModelTemplate(AutoPipelineBaseTemplate):
    def __init__(self, requirements=None, required_imports=None, default_values=None):
        """
        The __init__ function is used to initialize the class.
        It takes in a template, requirements, required_imports and default_values as arguments.
        The template argument is a string that contains the code for your function. 
        The requirements argument is an optional list of strings that contain any additional packages you need to install before running your function (e.g., ['pandas', 'numpy']). 
        The required_imports argument is an optional list of strings that contain any additional imports you need to run your function (e.g., ['import pandas as pd', 'import numpy as np
        
        :param self: Represent the instance of the class
        :param requirements: Specify the required packages for this template
        :param required_imports: Specify the imports that are required for the template to run
        :param default_values: Set the default values of the parameters that will be used in the template
        :return: The super() class
        """
        super().__init__(
            template=template,
            requirements=requirements,
            required_imports=required_imports,
            default_values=default_values
            )
    
 
