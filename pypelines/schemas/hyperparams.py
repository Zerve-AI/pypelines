from pydantic import BaseModel
from .constant_param import ConstantParam
from .numerical_param import NumericalParam
from .categorical_param import CategoricalParam

from .constant_param import ConstantParamAD
from .numerical_param import NumericalParamAD
from .categorical_param import CategoricalParamAD

from .categorical_param import CategoricalParamTSClassification
from .numerical_param import NumericalParamClassification
from .constant_param import ConstantParamTSClassification
from typing import List, Union


class HyperParams(BaseModel):
    params: List[Union[ConstantParam, NumericalParam, CategoricalParam]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'


class HyperParamsAD(BaseModel):
    params: List[Union[ConstantParamAD, NumericalParamAD, CategoricalParamAD]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

class HyperParamsTSClassification(BaseModel):
    params: List[Union[CategoricalParamTSClassification, NumericalParamClassification, ConstantParamTSClassification]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'
