from ..dataprep_base import DataPrepBase


class CategoricalImputer(DataPrepBase):
    def __init__(self):
        model_string = 'CategoricalImputer()'
        imports = '''from feature_engine.imputation import CategoricalImputer'''
        fe_type='imputation'
        super().__init__('CategoricalImputer', model_string, imports, fe_type)

