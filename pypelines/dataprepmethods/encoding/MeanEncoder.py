from ..dataprep_base import DataPrepBase


class MeanEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'MeanEncoder()'
        imports = '''from feature_engine.encoding import MeanEncoder\n\n\nencode = MeanEncoder(variables=None, missing_values='raise', ignore_format=False, unseen='ignore', smoothing=0.0)'''
        method='encoding'
        super().__init__('meanencoder', model_string, imports, method)

