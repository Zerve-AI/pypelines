from ..dataprep_base import DataPrepBase


class MatchCategories(DataPrepBase):
    def __init__(self):
        model_string = 'MatchCategories()'
        imports = '''feature_engine.preprocessing import MatchCategories'''
        method='preprocessing'
        super().__init__('MatchCategories', model_string, imports, method)

