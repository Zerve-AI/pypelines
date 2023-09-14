from ..dataprep_base import DataPrepBase


class DropHighPSIFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'DropHighPSIFeatures()'
        imports = '''from feature_engine.selection import DropHighPSIFeatures'''
        method='featureselection'
        super().__init__('DropHighPSIFeatures', model_string, imports, method)

