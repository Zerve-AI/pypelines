from ..dataprep_base import DataPrepBase


class CountFrequencyEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'CountFrequencyEncoder()'
        imports = '''from feature_engine.encoding import CountFrequencyEncoder\n\n\nencode = CountFrequencyEncoder(encoding_method='count', variables=None, missing_values='raise', ignore_format=False, unseen='ignore')'''
        method='encoding'
        super().__init__('countfrequencyencoder', model_string, imports, method)

