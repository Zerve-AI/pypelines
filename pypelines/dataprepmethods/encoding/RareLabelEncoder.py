from ..dataprep_base import DataPrepBase


class RareLabelEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'RareLabelEncoder()'
        imports = '''from feature_engine.encoding import RareLabelEncoder'''
        method='encoding'
        super().__init__('RareLabelEncoder', model_string, imports, method)

