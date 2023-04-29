# pypelines
Setup Steps:
1. Use pypelines_demo.ipynb to access the package
2. Update default_content.py with relevant config for the problem
  - 'dataset': 'train.csv', # add data frame name 
  - 'target_column': 'target', # add target column name
  - 'model_type': 'classification', # problem type - regression,classifiction currently supported
  - 'cross_validation': 5, # specify cross validation folds
  - 'selected_models': ['Logistic Regression','SVC'], # mention the models to be run. Refer below for supported models
  - 'completed_models': [],
  - 'classification': SklearnPipeline().get_settings_classification(),
  - 'regression': SklearnPipeline().get_settings_regression()

## Supported Models:
### Regression:
1. [Linear Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/linear_regression.py)
2. [Lasso Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/lasso_regression.py)
3. [Ridge Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/ridge_regression.py)
4. [Elastic Net Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/elastic_net_regression.py)

### Classification:
1. [Decision Tree](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/decision_tree.py)
2. [Logistic Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/logistic_regression.py)
3. [MLP](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/mlp.py)
4. [Random Forest](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/random_forest.py)
5. [Ridge Classifier](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/ridge_classification.py)
6. [SVC](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/svc.py)
7. [XGBoost](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/xgboost.py)

