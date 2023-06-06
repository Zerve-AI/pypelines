# What is pypelines
Pypelines is an open source automated machine learning training code generation utility.  It's intended to help data scientists get a fast start on building new models by providing boilerplate sklearn pipeline training code for a given dataset.

The generated code includes:
- Data preparation and feature engineering
	- Missing value imputation
	- Standardization
	- Cataegorical feature prep
	- Text parsing; e.g., TF-IDF
- K-fold cross validation
- Grid search
- Model training
- Model comparison

Training code is generated as follows:
```py
from pypelines.sklearn_pypeline import SupervisedPipeline
my_pypeline = SupervisedPipeline(data = your_dataframe,
                                 target = 'dependent_variable_name', 
				 model_type = 'classification' # or 'regression', 
				 nfolds = 5 # default is 5
				 )

my_pypeline.get_code()
```

`SupervisedPipeline()` can also be passed a list of model names through an optional `models` parameter.  If `models` is not specified, all available models will be included.

To see a listing of all available models, utilize `pypelines.classification_model_list()` and `pypelines.regression_model_list()`

## A few noteable pypeline object methods
- `my_pypeline.model_list()` returns a list of models to be included in the training code.
- `my_pypeline.get_hyperparameters()` returns a dictionary containing the grid search parameters for every model to be included in the training code.
- `my_pypeline.model_grid_search_settings(model_name)` returns a dictionary containing the grid search parameters of the specified model
- `my_pypeline.set_model_grid_search_settings(hyperparam_dict,model_name,path)` returns the model code with updated dictionary
- `my_pypeline.code_to_clipboard()` copies the training code to the clipboard.
- `my_pypeline.code_to_file('/path/to/filename.py')` saves the training code to a file.

## Supported Models:
See currently available models: [Regression](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/regression/) and [Classification](https://github.com/Zerve-AI/pypelines/blob/master/pypelines/sklearn/classification/)

