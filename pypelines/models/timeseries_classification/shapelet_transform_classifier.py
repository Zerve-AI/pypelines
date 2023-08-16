from ..model_base import TSClassificationModelBase, TSClassificationModelComparisonBase

ShapeletTransformClassifier_classification_hyperparams = {
    'numerical': [
        {'search': True, 'name': 'n_shapelet_samples', 'min': 1000, 'max': 10000, 'step': 2000},
        {'search': False, 'name': 'batch_size', 'min': 50, 'max': 100, 'step': 10}
    ],
    'categorical': [
        {'search': True, 'name': 'save_transformed_data', 'selected': [False], 'values': [True, False]}
    ]
}


class ShapeletTransformTSClassifier(TSClassificationModelBase):
    def __init__(self):
        model_string = 'ShapeletTransformClassifier()'
        imports = '''from sktime.classification.shapelet_based import ShapeletTransformClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ShapeletTransformClassifier', model_string, ShapeletTransformClassifier_classification_hyperparams, imports,model_type)

class ShapeletTransformTSClassifierComparison(TSClassificationModelComparisonBase):
    def __init__(self):
        model_string = 'ShapeletTransformClassifier()'
        imports = '''from sktime.classification.shapelet_based import ShapeletTransformClassifier\nfrom sklearn.model_selection import GridSearchCV\nfrom sklearn.metrics import accuracy_score,make_scorer,f1_score,precision_score,recall_score,roc_auc_score,roc_curve,auc\nimport matplotlib.pyplot as plt'''
        model_type ='Classification'
        super().__init__('ShapeletTransformClassifier', model_string, ShapeletTransformClassifier_classification_hyperparams, imports,model_type)