from ..dataprep_base import DataPrepBase


class DatetimeSubtraction(DataPrepBase):
    def __init__(self):
        model_string = 'DatetimeSubtraction()'
        imports = '''from feature_engine.datetime import DatetimeSubtraction'''
        method='datetime'
        super().__init__('DatetimeSubtraction', model_string, imports, method)

