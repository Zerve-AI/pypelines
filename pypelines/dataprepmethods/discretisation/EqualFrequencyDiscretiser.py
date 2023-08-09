from ..model_base import DataPreplBase


class EqualFrequencyDiscretiser(DataPreplBase):
    def __init__(self):
        model_string = 'EqualFrequencyDiscretiser()'
        imports = '''from feature_engine.discretisation import EqualFrequencyDiscretiser\ndiscret = EqualFrequencyDiscretiser(variables=None, q=10, return_object=False, return_boundaries=False, precision=3)'''
        method='discretisation'
        super().__init__('equalfrequencydiscretiser', model_string, imports, method)

