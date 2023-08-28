from ..dataprep_base import DataPrepBase


class CountFrequencyEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'CountFrequencyEncoder()'
        imports = '''from feature_engine.encoding import CountFrequencyEncoder'''
        method='encoding'
        super().__init__('countfrequencyencoder', model_string, imports, method)

