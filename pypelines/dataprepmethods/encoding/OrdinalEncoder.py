from ..model_base import DataPreplBase


class OrdinalEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'OrdinalEncoder()'
        imports = '''from feature_engine.encoding import OrdinalEncoder\n\n\nencode = OrdinalEncoder()'''
        outlier_type='encoding'
        super().__init__('ordinalencoder', model_string, imports, outlier_type)

