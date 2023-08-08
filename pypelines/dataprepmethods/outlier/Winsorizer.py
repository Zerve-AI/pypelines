from ..model_base import DataPreplBase



class WinsorizerOutlier(DataPreplBase):
    def __init__(self):
        model_string = 'Winsorizer()'
        imports = '''from feature_engine.outliers import Winsorizer\n\n\nout = Winsorizer(capping_method='mad', tail='both', fold=3)'''
        method='outlier'
        super().__init__('winsorizer', model_string, imports,method)

