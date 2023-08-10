from ..dataprep_base import DataPrepBase


class AddMissingIndicator(DataPrepBase):
    def __init__(self):
        model_string = 'AddMissingIndicator()'
        imports = '''from feature_engine.imputation import AddMissingIndicator'''
        fe_type='imputation'
        super().__init__('AddMissingIndicator', model_string, imports, fe_type)

