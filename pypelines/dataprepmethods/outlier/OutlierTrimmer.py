from ..model_base import DataPreplBase




class OutlierTrimmer(DataPreplBase):
    def __init__(self):
        model_string = 'OutlierTrimmer()'
        imports = '''from feature_engine.outliers import OutlierTrimmer\nout = OutlierTrimmer(capping_method='gaussian', tail='right', fold=3, variables=None, missing_values='ignore')'''
        method='outlier'
        super().__init__('outliertrimmer', model_string, imports, method)

