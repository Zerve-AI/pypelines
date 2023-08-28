from ..dataprep_base import DataPrepBase


class SelectByShuffling(DataPrepBase):
    def __init__(self):
        model_string = 'SelectByShuffling()'
        imports = '''from feature_engine.selection import SelectByShuffling\nfrom sklearn.ensemble import RandomForestClassifier'''
        method='featureselection'
        super().__init__('SelectByShuffling', model_string, imports, method)

