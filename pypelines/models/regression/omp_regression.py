from ..model_base import SklearnModelBase,SklearnModelComparisonBase


omp_regression_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_nonzero_coefs', 'min': 0, 'max': 10, 'step': 2},
    ],
    'categorical': [
        {'search': False, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
        {'search': False, 'name': 'normalize', 'selected': [False], 'values': [True,False]}
    ]
}

class OMPRegression(SklearnModelBase):
    def __init__(self):
        model_string = 'OrthogonalMatchingPursuit()'
        imports = '''from sklearn.linear_model import OrthogonalMatchingPursuit \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('omp_regression', model_string, omp_regression_hyperparams, imports,model_type)


class OMPRegressionComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'OrthogonalMatchingPursuit()'
        imports = '''from sklearn.linear_model import OrthogonalMatchingPursuit \nfrom sklearn.metrics import mean_squared_error,make_scorer,r2_score,explained_variance_score\nimport matplotlib.pyplot as plt'''
        model_type='Regression'
        super().__init__('omp_regression', model_string, omp_regression_hyperparams, imports,model_type)
