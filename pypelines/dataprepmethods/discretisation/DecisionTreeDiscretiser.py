from ..model_base import DataPreplBase


class DecisionTreeDiscretiser(DataPreplBase):
    def __init__(self):
        model_string = 'DecisionTreeDiscretiser()'
        imports = '''from feature_engine.discretisation import DecisionTreeDiscretiser\ndiscret = DecisionTreeDiscretiser(variables=None, cv=3, scoring='neg_mean_squared_error', param_grid=None, regression=True, random_state=None)'''
        method='discretisation'
        super().__init__('DecisionTreeDiscretiser', model_string, imports, method)

