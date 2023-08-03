from pydantic import BaseModel
from .constant_param import ConstantParam
from .numerical_param import NumericalParam
from .categorical_param import CategoricalParam

from .constant_param import ConstantParamAD
from .numerical_param import NumericalParamAD
from .categorical_param import CategoricalParamAD

from .categorical_param import CategoricalParamTSClassification
from .numerical_param import NumericalParamTSClassification
from .constant_param import ConstantParamTSClassification

from .categorical_param import CategoricalParamTSRegression
from .numerical_param import NumericalParamTSRegression
from .constant_param import ConstantParamTSRegression


from .categorical_param import CategoricalParamTSClustering
from .numerical_param import NumericalParamTSClustering
from .constant_param import ConstantParamTSClustering

from .constant_param import ConstantParamClustering
from .numerical_param import NumericalParamClustering
from .categorical_param import CategoricalParamClustering


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
    params: List[Union[CategoricalParamTSClassification, NumericalParamTSClassification, ConstantParamTSClassification]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'
    
class HyperParamsTSRegression(BaseModel):
    params: List[Union[CategoricalParamTSRegression, NumericalParamTSRegression, ConstantParamTSRegression]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'
    
class HyperParamsTSClustering(BaseModel):
    params: List[Union[CategoricalParamTSClustering, NumericalParamTSClustering, ConstantParamTSClustering]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

class HyperParamsClustering(BaseModel):
    params: List[Union[ConstantParamClustering, NumericalParamClustering, CategoricalParamClustering]]

    def __repr__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'

    def __str__(self):
        return f'{{\n{"".join([str(param) for param in self.params])}}}\n'
