from ..model_base import SklearnModelBase
from ..model_base import SklearnModelComparisonBase

mt_elastic_net_regression_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0.1, 'max': 1, 'step': 0.5},
        {'checked': True, 'name': 'l1_ratio', 'min': 0.0, 'max': 1.0, 'step': 0.5},
        {'checked': True, 'name': 'max_iter', 'min': 500, 'max': 1000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True, False]},
        {'checked': True, 'name': 'warm_start', 'selected': [False], 'values': [True, False]},
        {'checked': True, 'name': 'selection', 'selected': ['cyclic'], 'values': ['cyclic', 'random']}
    ]
}


class MTElasticNetRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'MultiTaskElasticNet()'
        imports = '''from sklearn.linear_model import MultiTaskElasticNet\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('mt_elastic_net_regression', model_string, mt_elastic_net_regression_hyperparams, imports,model_type)

class MTElasticNetRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'MultiTaskElasticNet()'
        imports = '''from sklearn.linear_model import MultiTaskElasticNet\nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport plotly.express as px\nimport plotly.graph_objects as go'''
        model_type='Regression'
        super().__init__('mt_elastic_net_regression', model_string, mt_elastic_net_regression_hyperparams, imports,model_type)