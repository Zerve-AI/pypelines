from ..dataprep_base import DataPrepBase


class WoEEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'WoEEncoder()'
        imports = '''from feature_engine.encoding import WoEEncoder\n\n\nencode = WoEEncoder(variables=None, ignore_format=False, unseen='ignore', fill_value=None)'''
        method='encoding'
        super().__init__('woeencoder', model_string, imports, method)

