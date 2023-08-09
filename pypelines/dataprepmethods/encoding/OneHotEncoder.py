from ..model_base import DataPreplBase


class OneHotEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'OneHotEncoder()'
        imports = '''from feature_engine.encoding import OneHotEncoder\n\n\nencode = OneHotEncoder(top_categories=None, drop_last=False, drop_last_binary=False, variables=None, ignore_format=False)[so'''
        method='encoding'
        super().__init__('onehotencoder', model_string, imports, method)

