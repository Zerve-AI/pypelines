from ..dataprep_base import DataPrepBase


class MeanEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'MeanEncoder()'
        imports = '''from feature_engine.encoding import MeanEncoder'''
        method='encoding'
        super().__init__('meanencoder', model_string, imports, method)

