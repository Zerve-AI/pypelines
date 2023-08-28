from ..dataprep_base import DataPrepBase


class DropCorrelatedFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'DropCorrelatedFeatures()'
        imports = '''from feature_engine.selection import DropCorrelatedFeatures'''
        method='featureselection'
        super().__init__('DropCorrelatedFeatures', model_string, imports, method)

