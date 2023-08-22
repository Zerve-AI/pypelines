from ..dataprep_base import DataPrepBase


class BoxCoxTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'BoxCoxTransformer()'
        imports = '''from feature_engine.transformation import BoxCoxTransformer'''
        method='transformer'
        super().__init__('BoxCoxTransformer', model_string, imports, method)

