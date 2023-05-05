from ..model_base import SklearnModelBase,SklearnModelComparisonBase


decision_tree_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'max_depth', 'min': 1, 'max': 10, 'step': 3},
        {'checked': False, 'name': 'min_samples_split', 'min': 0.1, 'max': 0.5, 'step': 0.2},
        {'checked': False, 'name': 'min_samples_leaf', 'min': 2, 'max': 10, 'step': 3},
    ],
    'categorical': [
        {'checked': True, 'name': 'max_features', 'selected': [None], 'values': ["auto", "sqrt", "log2"]},
        {'checked': False, 'name': 'splitter', 'selected': ["best"], 'values': ["best", "random"]}
    ]
}

class DecisionTreeRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'DecisionTreeRegressor()'
        imports = '''from sklearn.tree import DecisionTreeRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('decision_tree_regression', model_string, decision_tree_regression_hyperparams, imports,model_type)


class DecisionTreeRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'DecisionTreeRegressor()'
        imports = '''from sklearn.tree import DecisionTreeRegressor \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('decision_tree_regression', model_string, decision_tree_regression_hyperparams, imports,model_type)
