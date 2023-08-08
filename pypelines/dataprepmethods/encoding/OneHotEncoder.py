from ..model_base import DataPreplBase


class OneHotEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'OneHotEncoder()'
        imports = '''from feature_engine.encoding import OneHotEncoder\n\n\nencode = OneHotEncoder()'''
        method='encoding'
        super().__init__('onehotencoder', model_string, imports, method)

