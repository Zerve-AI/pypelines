from ..dataprep_base import DataPrepBase


class WindowFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'WindowFeatures()'
        imports = '''feature_engine.timeseries.forecasting import WindowFeatures'''
        method='forecasting'
        super().__init__('WindowFeatures', model_string, imports, method)

