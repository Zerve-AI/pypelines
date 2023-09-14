from ..dataprep_base import DataPrepBase


class DatetimeFeatures(DataPrepBase):
    def __init__(self):
        model_string = 'DatetimeFeatures()'
        imports = '''from feature_engine.datetime import DatetimeFeatures'''
        method='datetime'
        super().__init__('DatetimeFeatures', model_string, imports, method)

