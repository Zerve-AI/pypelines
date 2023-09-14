from ..dataprep_base import DataPrepBase


class YeoJohnsonTransformer(DataPrepBase):
    def __init__(self):
        model_string = 'YeoJohnsonTransformer()'
        imports = '''from feature_engine.transformation import YeoJohnsonTransformer'''
        method='transformer'
        super().__init__('YeoJohnsonTransformer', model_string, imports, method)

