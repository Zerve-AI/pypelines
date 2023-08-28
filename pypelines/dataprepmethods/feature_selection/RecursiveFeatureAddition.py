from ..dataprep_base import DataPrepBase


class RecursiveFeatureAddition(DataPrepBase):
    def __init__(self):
        model_string = 'RecursiveFeatureAddition()'
        imports = '''from feature_engine.selection import RecursiveFeatureAddition\nfrom sklearn.ensemble import RandomForestClassifier'''
        method='featureselection'
        super().__init__('RecursiveFeatureAddition', model_string, imports, method)

