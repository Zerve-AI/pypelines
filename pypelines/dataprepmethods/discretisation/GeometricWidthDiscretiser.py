from ..dataprep_base import DataPrepBase


class GeometricWidthDiscretiser(DataPrepBase):
    def __init__(self):
        model_string = 'GeometricWidthDiscretiser()'
        imports = '''from feature_engine.discretisation import GeometricWidthDiscretiser'''
        method='discretisation'
        super().__init__('GeometricWidthDiscretiser', model_string, imports, method)

