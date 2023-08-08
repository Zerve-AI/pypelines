from ..model_base import DataPreplBase


class ArbitraryCapperOutlier(DataPreplBase):
    def __init__(self):
        model_string = 'ArbitraryOutlierCapper()'
        imports = '''from feature_engine.outliers import ArbitraryOutlierCapper\n\n\nout = ArbitraryOutlierCapper(max_capping_dict=dict(x1 =  8),
                             min_capping_dict=dict(x1 = 2))'''
        method='outlier'
        super().__init__('arbitraryoutliercapper', model_string, imports, method)

