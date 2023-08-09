from ..model_base import DataPreplBase


class ArbitraryCapperOutlier(DataPreplBase):
    def __init__(self):
        model_string = 'ArbitraryOutlierCapper()'
        imports = '''from feature_engine.outliers import ArbitraryOutlierCapper\nout = ArbitraryOutlierCapper(max_capping_dict=None, min_capping_dict=None, missing_values='ignore')'''
        method='outlier'
        super().__init__('arbitraryoutliercapper', model_string, imports, method)

