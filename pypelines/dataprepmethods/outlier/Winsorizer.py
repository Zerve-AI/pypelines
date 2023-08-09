from ..model_base import DataPreplBase



class WinsorizerOutlier(DataPreplBase):
    def __init__(self):
        model_string = 'Winsorizer()'
        imports = '''from feature_engine.outliers import Winsorizer\nout = Winsorizer(capping_method='gaussian', tail='right', fold=3, add_indicators=False, variables=None, missing_values='ignore')'''
        method='outlier'
        super().__init__('winsorizer', model_string, imports,method)

