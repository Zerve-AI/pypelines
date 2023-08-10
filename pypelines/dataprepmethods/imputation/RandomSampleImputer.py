from ..dataprep_base import DataPrepBase


class RandomSampleImputer(DataPrepBase):
    def __init__(self):
        model_string = 'RandomSampleImputer()'
        imports = '''from feature_engine.imputation import RandomSampleImputer'''
        fe_type='imputation'
        super().__init__('RandomSampleImputer', model_string, imports, fe_type)

