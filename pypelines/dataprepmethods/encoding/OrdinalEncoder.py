from ..dataprep_base import DataPrepBase


class OrdinalEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'OrdinalEncoder()'
        imports = '''from feature_engine.encoding import OrdinalEncoder'''
        method='encoding'
        super().__init__('ordinalencoder', model_string, imports, method)

