from ..model_base import DataPreplBase




class OutlierTrimmer(DataPreplBase):
    def __init__(self):
        model_string = 'OutlierTrimmer()'
        imports = '''from feature_engine.outliers import OutlierTrimmer\n\n\nout = OutlierTrimmer(capping_method='gaussian', tail='left', fold=3)'''
        outlier_type='outlier'
        super().__init__('outliertrimmer', model_string, imports, outlier_type)

