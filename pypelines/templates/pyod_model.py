from .template_base import AutoPipelineBaseTemplate


template = '''
{{imports}}

def scorer_f(estimator, X_test):   #dummy scorer for unsupervised model gridsearch
      return 1


{{prefix}}_param_grid = {{hyperparams}}

{{prefix}}_model = {{prefix}}()

# Perform grid search with cross-validation
{{prefix}}_grid_search = GridSearchCV({{prefix}}_model,
                                      {{prefix}}_param_grid, 
                                      scoring=scorer_f, 
                                      verbose=3)
{{prefix}}_grid_search.fit(x_train_preprocessed)

# Get the best hyperparameters
{{prefix}}_best_estimator = {{prefix}}_grid_search.best_estimator_

# get the prediction labels and outlier scores of the training data
{{prefix}}_y_train_pred = {{prefix}}_best_estimator.labels_ 
{{prefix}}_y_train_scores = {{prefix}}_best_estimator.decision_scores_

# get the prediction on the test data
{{prefix}}_y_test_pred = {{prefix}}_best_estimator.predict(y_train_preprocessed)
{{prefix}}_y_test_pred_proba = {{prefix}}_best_estimator.predict_proba(y_train_preprocessed) 
{{prefix}}_y_test_scores = {{prefix}}_best_estimator.decision_function(y_train_preprocessed) 

'''

class PYODModelTemplate(AutoPipelineBaseTemplate):
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
    
 
