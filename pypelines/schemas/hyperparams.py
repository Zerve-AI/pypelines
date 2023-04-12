from pydantic import BaseModel
from .constant_param import ConstantParam
from .numerical_param import NumericalParam
from .categorical_param import CategoricalParam
from typing import List, Union


class HyperParams(BaseModel):
    params: List[Union[ConstantParam, NumericalParam, CategoricalParam]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'


