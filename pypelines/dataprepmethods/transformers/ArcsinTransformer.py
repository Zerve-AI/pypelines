from ..dataprep_base import DataPrepBase


class ArcsinTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'ArcsinTransformer()'
        imports = '''from feature_engine.transformation import ArcsinTransformer'''
        method='transformer'
        super().__init__('ArcsinTransformer', model_string, imports, method)

