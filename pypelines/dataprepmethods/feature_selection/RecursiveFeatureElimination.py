from ..dataprep_base import DataPrepBase


class RecursiveFeatureElimination(DataPrepBase):
    def __init__(self):
        model_string = 'RecursiveFeatureElimination()'
        imports = '''from feature_engine.selection import RecursiveFeatureElimination\nfrom sklearn.ensemble import RandomForestClassifier'''
        method='featureselection'
        super().__init__('RecursiveFeatureElimination', model_string, imports, method)

