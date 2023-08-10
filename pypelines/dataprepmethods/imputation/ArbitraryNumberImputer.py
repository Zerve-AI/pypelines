from ..dataprep_base import DataPrepBase


class ArbitraryNumberImputer(DataPrepBase):
    def __init__(self):
        model_string = 'ArbitraryNumberImputer()'
        imports = '''from feature_engine.imputation import ArbitraryNumberImputer'''
        fe_type='imputation'
        super().__init__('ArbitraryNumberImputer', model_string, imports, fe_type)

