from ..dataprep_base import DataPrepBase


class DecisionTreeEncoder(DataPrepBase):
    def __init__(self):
        model_string = 'DecisionTreeEncoder()'
        imports = '''from feature_engine.encoding import DecisionTreeEncoder\n\n\nencode = DecisionTreeEncoder(encoding_method='arbitrary', cv=3, scoring='neg_mean_squared_error', param_grid=None, regression=True, random_state=None, variables=None, ignore_format=False)'''
        method='encoding'
        super().__init__('decisiontreeencoder', model_string, imports, method)

