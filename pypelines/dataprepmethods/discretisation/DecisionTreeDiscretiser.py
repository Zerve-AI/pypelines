from ..dataprep_base import DataPrepBase


class DecisionTreeDiscretiser(DataPrepBase):
    def __init__(self):
        model_string = 'DecisionTreeDiscretiser()'
        imports = '''from feature_engine.discretisation import DecisionTreeDiscretiser'''
        method='discretisation'
        super().__init__('DecisionTreeDiscretiser', model_string, imports, method)

