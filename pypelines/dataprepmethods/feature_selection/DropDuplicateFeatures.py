from ..dataprep_base import DataPrepBase


class DropDuplicateFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'DropDuplicateFeatures()'
        imports = '''from feature_engine.selection import DropDuplicateFeatures'''
        method='featureselection'
        super().__init__('DropDuplicateFeatures', model_string, imports, method)

