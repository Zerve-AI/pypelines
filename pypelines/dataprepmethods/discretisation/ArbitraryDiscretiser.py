from ..dataprep_base import DataPrepBase


class ArbitraryDiscretiser(DataPrepBase):
    def __init__(self):
        model_string = 'ArbitraryDiscretiser()'
        imports = '''from feature_engine.discretisation import ArbitraryDiscretiser'''
        method='discretisation'
        super().__init__('arbitrarydiscretiser', model_string, imports, method)

