from ..dataprep_base import DataPrepBase


class LagFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'LagFeatures()'
        imports = '''from feature_engine.timeseries.forecasting import LagFeatures'''
        method='forecasting'
        super().__init__('LagFeatures', model_string, imports, method)

