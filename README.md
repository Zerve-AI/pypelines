# pypelines
Setup Steps:
1. Use pypelines_demo.ipynb to access the package
2. Update default_content.py with relevant config for the problem
  - 'dataset': 'train.csv', #add data frame name 
  - 'target_column': 'target', #add target column name
  - 'model_type': 'classification', #problem type - regression,classifiction currently supported
  - 'cross_validation': 5, #specify cross validation folds
  - 'selected_models': ['Logistic Regression','SVC'], #mention the models to be run. Refer below for supported models
  - 'completed_models': [],
  - 'classification': SklearnPipeline().get_settings_classification(),
  - 'regression': SklearnPipeline().get_settings_regression()

## Supported Models:
### Regression:
1. ["linear_regression"]("https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/linear_regression.py")
2. [lasso_regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/lasso_regression.py)
3. [ridge_regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/ridge_regression.py)
4. [elastic_net_regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/elastic_net_regression.py)

