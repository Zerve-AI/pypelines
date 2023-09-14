from ..dataprep_base import DataPrepBase


class LogTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'LogTransformer()'
        imports = '''from feature_engine.transformation import LogTransformer'''
        method='transformer'
        super().__init__('LogTransformer', model_string, imports, method)

