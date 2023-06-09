from ..model_base import SklearnModelBase,SklearnModelComparisonBase


decision_tree_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'max_depth', 'min': 1, 'max': 10, 'step': 3},
        {'search': False, 'name': 'min_samples_split', 'min': 0.1, 'max': 0.5, 'step': 0.2},
        {'search': False, 'name': 'min_samples_leaf', 'min': 2, 'max': 10, 'step': 3},
    ],
    'categorical': [
        {'search': True, 'name': 'max_features', 'selected': ["auto"], 'values': ["auto", "sqrt", "log2"]},
        {'search': False, 'name': 'splitter', 'selected': ["best"], 'values': ["best", "random"]}
    ]
}

class DecisionTreeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'DecisionTreeRegressor()'
        imports = '''from sklearn.tree import DecisionTreeRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('decision_tree_regression', model_string, decision_tree_regression_hyperparams, imports,model_type)


class DecisionTreeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'DecisionTreeRegressor()'
        imports = '''from sklearn.tree import DecisionTreeRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('decision_tree_regression', model_string, decision_tree_regression_hyperparams, imports,model_type)
