from ..model_base import DataPreplBase


class MeanEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'MeanEncoder()'
        imports = '''from feature_engine.encoding import MeanEncoder\n\n\nencode = MeanEncoder()'''
        outlier_type='encoding'
        super().__init__('meanencoder', model_string, imports, outlier_type)

