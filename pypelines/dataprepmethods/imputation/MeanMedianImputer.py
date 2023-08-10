from ..dataprep_base import DataPrepBase


class MeanMedianImputer(DataPrepBase):
    def __init__(self):
        model_string = 'MeanMedianImputer()'
        imports = '''from feature_engine.imputation import MeanMedianImputer'''
        fe_type='imputation'
        super().__init__('MeanMedianImputer', model_string, imports, fe_type)

