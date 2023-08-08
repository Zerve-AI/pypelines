from ..model_base import DataPreplBase


class RareLabelEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'RareLabelEncoder()'
        imports = '''from feature_engine.encoding import RareLabelEncoder\n\n\nencode = RareLabelEncoder()'''
        method='encoding'
        super().__init__('RareLabelEncoder', model_string, imports, method)

