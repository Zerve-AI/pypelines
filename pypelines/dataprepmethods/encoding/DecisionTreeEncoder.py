from ..model_base import DataPreplBase


class DecisionTreeEncoder(DataPreplBase):
    def __init__(self):
        model_string = 'DecisionTreeEncoder()'
        imports = '''from feature_engine.encoding import DecisionTreeEncoder\n\n\nencode = DecisionTreeEncoder()'''
        method='encoding'
        super().__init__('decisiontreeencoder', model_string, imports, method)

