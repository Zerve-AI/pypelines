from ..dataprep_base import DataPrepBase


class SelectBySingleFeaturePerformance(DataPrepBase):
    def __init__(self):
        model_string = 'SelectBySingleFeaturePerformance()'
        imports = '''from feature_engine.selection import SelectBySingleFeaturePerformance\nfrom sklearn.ensemble import RandomForestClassifier'''
        method='featureselection'
        super().__init__('SelectBySingleFeaturePerformance', model_string, imports, method)

