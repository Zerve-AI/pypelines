from ..dataprep_base import DataPrepBase



class WinsorizerOutlier(DataPrepBase):
    def __init__(self):
        model_string = 'Winsorizer()'
        imports = '''from feature_engine.outliers import Winsorizer'''
        method='outlier'
        super().__init__('winsorizer', model_string, imports,method)

