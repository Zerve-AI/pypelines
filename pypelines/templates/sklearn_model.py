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
{{prefix}}_actual_predicted_plot = px.scatter(x=y_test, y={{prefix}}_predictions.iloc[:,0])
{{prefix}}_actual_predicted_plot.add_shape(type="line", line=dict(dash='dash'),x0=y.min(), y0=y.min(), x1=y.max(), y1=y.max())
{{prefix}}_actual_predicted_plot.update_layout(title="Actual vs Predicted",xaxis_title="Actual",yaxis_title="Predicted")
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
{{prefix}}_roc_auc_plot = px.area(
    x=fpr, y=tpr,
    title=f'ROC Curve (AUC={auc(fpr, tpr):.4f})',
    labels=dict(x='False Positive Rate', y='True Positive Rate'),
    width=700, height=500
)
{{prefix}}_roc_auc_plot.add_shape(
    type='line', line=dict(dash='dash'),
    x0=0, x1=1, y0=0, y1=1
)
{{prefix}}_roc_auc_plot.update_yaxes(scaleanchor="x", scaleratio=1)
{{prefix}}_roc_auc_plot.update_xaxes(constrain='domain')
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
    
 
