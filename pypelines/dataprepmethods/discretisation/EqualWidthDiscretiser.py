from ..model_base import DataPreplBase


class EqualWidthDiscretiser(DataPreplBase):
    def __init__(self):
        model_string = 'EqualWidthDiscretiser()'
        imports = '''from feature_engine.discretisation import EqualWidthDiscretiser\ndiscret = EqualWidthDiscretiser(variables=None, bins=10, return_object=False, return_boundaries=False, precision=3)'''
        method='discretisation'
        super().__init__('equalwidthdiscretiser', model_string, imports, method)

