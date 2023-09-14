from ..dataprep_base import DataPrepBase


class ArbitraryCapperOutlier(DataPrepBase):
    def __init__(self):
        model_string = 'ArbitraryOutlierCapper()'
        imports = '''from feature_engine.outliers import ArbitraryOutlierCapper'''
        method='outlier'
        super().__init__('arbitraryoutliercapper', model_string, imports, method)

