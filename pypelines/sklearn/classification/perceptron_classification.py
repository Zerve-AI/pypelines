from ..model_base import SklearnModelBase, SklearnModelComparisonBase

perceptron_classification_hyperparams = {
    'numerical': [
        {'checked': True, 'name': 'alpha', 'min': 0, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'l1_ratio', 'min': 0, 'max': 1, 'step': 0.1},
        {'checked': True, 'name': 'max_iter', 'min': 1000, 'max': 10000, 'step': 100},
    ],
    'categorical': [
        {'checked': True, 'name': 'fit_intercept', 'selected': [True], 'values': [True,False]},
    ]
}


class PerceptronClassification(SklearnModelBase):
    def __init__(self):
        model_string = 'Perceptron()'
        imports = '''from sklearn.linear_model import Perceptron\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('perceptron_classifier', model_string, perceptron_classification_hyperparams, imports,model_type)

class PerceptronClassificationComparison(SklearnModelComparisonBase):
    def __init__(self):
        model_string = 'Perceptron()'
        imports = '''from sklearn.linear_model import Perceptron\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport plotly.express as px'''
        model_type ='Classification'
        super().__init__('perceptron_classifier', model_string, perceptron_classification_hyperparams, imports,model_type)