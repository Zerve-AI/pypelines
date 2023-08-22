from ..dataprep_base import DataPrepBase


class LogCpTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'LogCpTransformer()'
        imports = '''from feature_engine.transformation import LogCpTransformer'''
        method='transformer'
        super().__init__('LogCpTransformer', model_string, imports, method)

