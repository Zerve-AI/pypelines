from ..dataprep_base import DataPrepBase


class StringSimilarityEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'StringSimilarityEncoder()'
        imports = '''from feature_engine.encoding import StringSimilarityEncoder'''
        method='encoding'
        super().__init__('stringsimilarityencoder', model_string, imports, method)

