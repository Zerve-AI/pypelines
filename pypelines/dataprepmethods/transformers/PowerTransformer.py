from ..dataprep_base import DataPrepBase


class PowerTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'PowerTransformer()'
        imports = '''from feature_engine.transformation import PowerTransformer'''
        method='transformer'
        super().__init__('PowerTransformer', model_string, imports, method)

