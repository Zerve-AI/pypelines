from ..model_base import DataPreplBase


class CountFrequencyEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'CountFrequencyEncoder()'
        imports = '''from feature_engine.encoding import CountFrequencyEncoder\n\n\nencode = CountFrequencyEncoder()'''
        outlier_type='encoding'
        super().__init__('countfrequencyencoder', model_string, imports, outlier_type)

