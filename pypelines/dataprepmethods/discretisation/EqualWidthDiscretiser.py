from ..dataprep_base import DataPrepBase


class EqualWidthDiscretiser(DataPrepBase):
    def __init__(self):
        model_string = 'EqualWidthDiscretiser()'
        imports = '''from feature_engine.discretisation import EqualWidthDiscretiser'''
        method='discretisation'
        super().__init__('equalwidthdiscretiser', model_string, imports, method)

