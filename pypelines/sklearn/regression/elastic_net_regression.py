from ..model_base import SklearnModelBase
from ..model_base import SklearnModelComparisonBase

elastic_net_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'alpha', 'min': 0.1, 'max': 2, 'step': 0.5},
        {'search': True, 'name': 'l1_ratio', 'min': 0.1, 'max': 1.0, 'step': 0.3},
        {'search': False, 'name': 'max_iter', 'min': 500, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'search': False, 'name': 'selection', 'selected': ['cyclic'], 'values': ['cyclic', 'random']}
    ]
}


class ElasticNetRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'ElasticNet()'
        imports = '''from sklearn.linear_model import ElasticNet\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('elastic_net_regression', model_string, elastic_net_regression_hyperparams, imports,model_type)

class ElasticNetRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'ElasticNet()'
        imports = '''from sklearn.linear_model import ElasticNet\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('elastic_net_regression', model_string, elastic_net_regression_hyperparams, imports,model_type)