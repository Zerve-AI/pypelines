from ..dataprep_base import DataPrepBase


class SmartCorrelatedSelection(DataPrepBase):
    def __init__(self):
        model_string = 'SmartCorrelatedSelection()'
        imports = '''from feature_engine.selection import SmartCorrelatedSelection'''
        method='featureselection'
        super().__init__('SmartCorrelatedSelection', model_string, imports, method)

