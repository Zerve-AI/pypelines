from ..model_base import DataPreplBase


class OrdinalEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'OrdinalEncoder()'
        imports = '''from feature_engine.encoding import OrdinalEncoder\n\n\nencode = OrdinalEncoder(encoding_method='ordered', variables=None, missing_values='raise', ignore_format=False, unseen='ignore')'''
        method='encoding'
        super().__init__('ordinalencoder', model_string, imports, method)

