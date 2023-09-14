from ..dataprep_base import DataPrepBase


class EndTailImputer(DataPrepBase):
    def __init__(self):
        model_string = 'EndTailImputer()'
        imports = '''from feature_engine.imputation import EndTailImputer'''
        fe_type='imputation'
        super().__init__('EndTailImputer', model_string, imports, fe_type)

