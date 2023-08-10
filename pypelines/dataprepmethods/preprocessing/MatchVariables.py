from ..dataprep_base import DataPrepBase


class MatchVariables(DataPrepBase):
    def __init__(self):
        model_string = 'MatchVariables()'
        imports = '''from feature_engine.preprocessing import MatchVariables'''
        method='preprocessing'
        super().__init__('MatchVariables', model_string, imports, method)

