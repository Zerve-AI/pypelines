from ..dataprep_base import DataPrepBase


class DropConstantFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'DropConstantFeatures()'
        imports = '''from feature_engine.selection import DropConstantFeatures'''
        method='featureselection'
        super().__init__('DropConstantFeatures', model_string, imports, method)

