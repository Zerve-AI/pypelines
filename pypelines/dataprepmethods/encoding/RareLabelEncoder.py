from ..model_base import DataPreplBase


class RareLabelEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'RareLabelEncoder()'
        imports = '''from feature_engine.encoding import RareLabelEncoder\n\n\nencode = RareLabelEncoder(tol=0.05, n_categories=10, max_n_categories=None, replace_with='Rare', variables=None, missing_values='raise', ignore_format=False)'''
        method='encoding'
        super().__init__('RareLabelEncoder', model_string, imports, method)

