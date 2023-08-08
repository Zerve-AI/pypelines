from ..model_base import DataPreplBase


class StringSimilarityEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'StringSimilarityEncoder()'
        imports = '''from feature_engine.encoding import StringSimilarityEncoder\n\n\nencode = StringSimilarityEncoder())'''
        method='encoding'
        super().__init__('stringsimilarityencoder', model_string, imports, method)

