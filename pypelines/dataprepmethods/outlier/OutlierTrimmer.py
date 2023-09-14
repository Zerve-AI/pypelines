from ..dataprep_base import DataPrepBase




class OutlierTrimmer(DataPrepBase):
    def __init__(self):
        model_string = 'OutlierTrimmer()'
        imports = '''from feature_engine.outliers import OutlierTrimmer'''
        method='outlier'
        super().__init__('outliertrimmer', model_string, imports, method)

