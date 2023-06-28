from .template_base import AutoPipelineBaseTemplate



template = '''
{{imports}}
cv = ExpandingWindowSplitter(fh={{forecast_horizon}})

{{prefix}}_param_grid = {{hyperparams}}

{{prefix}}_model = {{prefix}}()

{{prefix}}_gscv = ForecastingGridSearchCV(
    forecaster={{prefix}}_model,
    param_grid={{prefix}}_param_grid,
    cv=cv,
    verbose=1)
{{prefix}}_gscv.fit(y_train_preprocessed)
{{prefix}}_performance_metrics = {{prefix}}_gscv.cv_results_
{{prefix}}_performance_metrics['model'] = {{prefix}}

model_comparison_list.append({{prefix}}_performance_metrics)

# get the prediction on the test data
{{prefix}}_y_pred = {{prefix}}_gscv.predict(fh={{forecast_horizon}})


{{prefix}}_val = pd.concat([y_train_preprocessed,{{prefix}}_y_pred])
{{prefix}}_val = {{prefix}}_val.reset_index()

# Example time series data
{{prefix}}_timestamps = {{prefix}}_val['index'].astype(str)  # List or array of timestamps
{{prefix}}_values = {{prefix}}_val[f'{target_col}']  # List or array of corresponding values

# Example two time points to differentiate
start_time = np.datetime64(y_train_preprocessed.reset_index()['Date'].astype(str)[0])
end_time = np.datetime64(y_train_preprocessed.reset_index()['Date'].astype(str)[143])

# Convert timestamps to datetime objects
{{prefix}}_timestamps = [np.datetime64(ts) for ts in {{prefix}}_timestamps]
{{prefix}}_mape = {{prefix}}_gscv.cv_results_['mean_test_MeanAbsolutePercentageError']
mape = {{prefix}}_mape.to_list()[0]

# Create color list for segments
colors = ['lightblue' if (start_time <= ts <= end_time) else 'orange' for ts in {{prefix}}_timestamps]

# Plot the time series with differentiated colors
plt.figure(figsize=(10, 6))
plt.plot({{prefix}}_timestamps, {{prefix}}_values, color='lightblue')
plt.scatter({{prefix}}_timestamps, {{prefix}}_values, color=colors)
plt.xlabel('years')
plt.ylabel(f'{target_col}')
plt.title(f'Forecast with {{prefix}}')
plt.annotate(f'MAPE: {mape:.2f}%', xy=(0.05, 0.9), xycoords='axes fraction')
plt.show()


'''

class TSForecastModelTemplate(AutoPipelineBaseTemplate):
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
    
 
