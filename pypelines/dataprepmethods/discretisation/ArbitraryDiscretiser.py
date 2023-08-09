from ..model_base import DataPreplBase


class ArbitraryDiscretiser(DataPreplBase):
    def __init__(self):
        model_string = 'ArbitraryDiscretiser()'
        imports = '''from feature_engine.discretisation import ArbitraryDiscretiser\ndiscret = ArbitraryDiscretiser(binning_dict, return_object=False, return_boundaries=False, precision=3, errors='ignore')'''
        method='discretisation'
        super().__init__('arbitrarydiscretiser', model_string, imports, method)

