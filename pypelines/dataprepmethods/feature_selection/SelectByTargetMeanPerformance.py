from ..dataprep_base import DataPrepBase


class SelectByTargetMeanPerformance(DataPrepBase):
    def __init__(self):
        model_string = 'SelectByTargetMeanPerformance()'
        imports = '''from feature_engine.selection import SelectByTargetMeanPerformance'''
        method='featureselection'
        super().__init__('SelectByTargetMeanPerformance', model_string, imports, method)

