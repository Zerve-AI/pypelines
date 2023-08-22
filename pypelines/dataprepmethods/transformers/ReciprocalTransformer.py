from ..dataprep_base import DataPrepBase


class ReciprocalTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'ReciprocalTransformer()'
        imports = '''from feature_engine.transformation import ReciprocalTransformer'''
        method='transformer'
        super().__init__('ReciprocalTransformer', model_string, imports, method)

