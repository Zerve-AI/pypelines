from ..dataprep_base import DataPrepBase


class OneHotEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'OneHotEncoder()'
        imports = '''from feature_engine.encoding import OneHotEncoder'''
        method='encoding'
        super().__init__('onehotencoder', model_string, imports, method)

