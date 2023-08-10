from ..dataprep_base import DataPrepBase


class EqualFrequencyDiscretiser(DataPrepBase):
    def __init__(self):
        model_string = 'EqualFrequencyDiscretiser()'
        imports = '''from feature_engine.discretisation import EqualFrequencyDiscretiser'''
        method='discretisation'
        super().__init__('equalfrequencydiscretiser', model_string, imports, method)

