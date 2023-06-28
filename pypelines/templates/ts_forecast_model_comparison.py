from .template_base import AutoPipelineBaseTemplate

# table = pd.concat([ARIMA_gscv.cv_results_,TrendForecaster_gscv.cv_results_, NaiveForecaster_gscv.cv_results_])
template = '''
table = pd.concat(model_comparison_list)
table = table.sort_values('mean_test_MeanAbsolutePercentageError', ascending=True)
print(table)
print(f"The best model is {table['model'].iloc[0]} with MAPE of {table['mean_test_MeanAbsolutePercentageError'].iloc[0]:1f} % and predict time of {table['mean_pred_time'].iloc[0]:1f}")

'''

class TSForecastModelComparisonTemplate(AutoPipelineBaseTemplate):
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
    
 
