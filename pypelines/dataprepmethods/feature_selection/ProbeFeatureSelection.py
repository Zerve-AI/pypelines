from ..dataprep_base import DataPrepBase


class ProbeFeatureSelection(DataPrepBase):
    def __init__(self):
        model_string = 'ProbeFeatureSelection()'
        imports = '''from feature_engine.selection import ProbeFeatureSelection\nfrom sklearn.linear_model import LogisticRegression'''
        method='featureselection'
        super().__init__('ProbeFeatureSelection', model_string, imports, method)

