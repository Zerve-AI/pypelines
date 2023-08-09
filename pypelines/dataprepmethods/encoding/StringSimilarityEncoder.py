from ..model_base import DataPreplBase


class StringSimilarityEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'StringSimilarityEncoder()'
        imports = '''from feature_engine.encoding import StringSimilarityEncoder\n\n\nencode = StringSimilarityEncoder(top_categories=None, keywords=None, missing_values='impute', variables=None, ignore_format=False)'''
        method='encoding'
        super().__init__('stringsimilarityencoder', model_string, imports, method)

