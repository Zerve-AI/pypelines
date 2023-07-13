from .template_base import AutoPipelineBaseTemplate


template = '''
{{imports}}
{{prefix}}_param_grid = {{hyperparams}}
{{prefix}}_model = {{prefix}}()

# Create the grid search
{{prefix}}_grid_search = GridSearchCV(estimator={{prefix}}_model, param_grid={{prefix}}_param_grid, cv={{cross_validation}}, scoring=make_scorer({{metric}}), verbose=3)
{{prefix}}_grid_search.fit(X_train, y_train)

# Get the best hyperparameters
{{prefix}}_best_estimator = {{prefix}}_grid_search.best_estimator_

# Store results as a dataframe  
{{prefix}}_search_results = pd.DataFrame({{prefix}}_grid_search.cv_results_)


# Generate Predictions
{{prefix}}_predictions = {{prefix}}_best_estimator.predict(X_test)
{{prefix}}_predictions_df = pd.DataFrame({{prefix}}_best_estimator.predict(X_test))

# Generate Model Metrics
{{prefix}}_r2_score = r2_score(y_test, {{prefix}}_predictions_df.iloc[:,0])
{{prefix}}_mean_squared_error = mean_squared_error(y_test, {{prefix}}_predictions_df.iloc[:,0])
{{prefix}}_explained_variance_score = explained_variance_score(y_test, {{prefix}}_predictions_df.iloc[:,0])
{{prefix}}_performance_metrics = [['{{prefix}}','r2_score', {{prefix}}_r2_score], 
                                  ['{{prefix}}','mean_squared_error',{{prefix}}_mean_squared_error],
                                  ['{{prefix}}','explained_variance_score', {{prefix}}_explained_variance_score]]
{{prefix}}_performance_metrics = pd.DataFrame({{prefix}}_performance_metrics, columns=['model','metric', 'value'])

# Generate Actual vs Predicted Plot
{{prefix}}_actual_predicted_plot, {{prefix}}_actual_predicted_plot_ax = plt.subplots()
{{prefix}}_actual_predicted_plot = {{prefix}}_actual_predicted_plot_ax.scatter(x=y_test, y={{prefix}}_predictions_df.iloc[:,0], alpha=0.5)
# Add diagonal line
{{prefix}}_actual_predicted_plot_ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', alpha=0.5)
# Set axis labels and title
{{prefix}}_actual_predicted_plot_ax.set_xlabel('Actual')
{{prefix}}_actual_predicted_plot_ax.set_ylabel('Predicted')
{{prefix}}_actual_predicted_plot_ax.set_title(f'{{prefix}} Actual vs. Predicted')
plt.show(block=False)

# Generate Decile Lift Chart
# Calculate the deciles based on the residuals
{{prefix}}_deciles = np.percentile({{prefix}}_predictions, np.arange(0, 100, 10))
# Calculate the mean actual and predicted values for each decile
{{prefix}}_mean_actual = []
{{prefix}}_mean_predicted = []
for i in range(len({{prefix}}_deciles) - 1):
    mask = ({{prefix}}_predictions >= {{prefix}}_deciles[i]) & ({{prefix}}_predictions < {{prefix}}_deciles[i + 1])
    {{prefix}}_mean_actual.append(np.mean(y_test[mask]))
    {{prefix}}_mean_predicted.append(np.mean({{prefix}}_predictions[mask]))

# Create a bar chart of the mean actual and predicted values for each decile
{{prefix}}_lift_plot, {{prefix}}_lift_plot_ax = plt.subplots()
{{prefix}}_lift_plot_ax.bar(np.arange(len({{prefix}}_mean_actual)), {{prefix}}_mean_actual, label='Actual')
{{prefix}}_lift_plot_ax.plot(np.arange(len({{prefix}}_mean_predicted)), {{prefix}}_mean_predicted, color='red', linewidth=2, label='Predicted')
{{prefix}}_lift_plot_ax.set_xlabel('Deciles')
{{prefix}}_lift_plot_ax.set_ylabel('Mean')
{{prefix}}_lift_plot_ax.set_title(f'{{prefix}} Decile Analysis Chart')
{{prefix}}_lift_plot_ax.legend()
plt.show(block=False)


model_comparison_list.append({{prefix}}_performance_metrics)
'''

class TSRegressionModelTemplate(AutoPipelineBaseTemplate):
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
    
 
