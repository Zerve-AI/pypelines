from ..dataprep_base import DataPrepBase


class SelectByInformationValue(DataPrepBase):
    def __init__(self):
        model_string = 'SelectByInformationValue()'
        imports = '''from feature_engine.selection import SelectByInformationValue'''
        method='featureselection'
        super().__init__('SelectByInformationValue', model_string, imports, method)

