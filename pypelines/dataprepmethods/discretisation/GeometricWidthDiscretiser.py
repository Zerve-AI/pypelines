from ..model_base import DataPreplBase


class GeometricWidthDiscretiser(DataPreplBase):
    def __init__(self):
        model_string = 'GeometricWidthDiscretiser()'
        imports = '''from feature_engine.discretisation import GeometricWidthDiscretiser\ndiscret = GeometricWidthDiscretiser(variables=None, bins=10, return_object=False, return_boundaries=False, precision=7)'''
        method='discretisation'
        super().__init__('GeometricWidthDiscretiser', model_string, imports, method)

