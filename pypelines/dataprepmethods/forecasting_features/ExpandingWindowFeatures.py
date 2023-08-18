from ..dataprep_base import DataPrepBase


class ExpandingWindowFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'ExpandingWindowFeatures()'
        imports = '''feature_engine.timeseries.forecasting import ExpandingWindowFeatures'''
        method='forecasting'
        super().__init__('ExpandingWindowFeatures', model_string, imports, method)

