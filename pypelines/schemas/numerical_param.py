from pydantic import BaseModel
from typing import List, Union


class NumericalParam(BaseModel):
    prefix: str
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.prefix}__{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.prefix}__{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.prefix}__{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.prefix}__{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'
    

class NumericalParamAD(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'
 
class NumericalParamTSF(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'
     
class NumericalParamTSClassification(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

class NumericalParamTSRegression(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'
    
class NumericalParamTSClustering(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

class NumericalParamClustering(BaseModel):
    name: str
    min: Union[float, int]
    max: Union[float, int]
    step: Union[float, int]

    def __repr__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'

    def __str__(self):
        '''make a int if possible'''
        if self.min.is_integer() and self.max.is_integer() and self.step.is_integer():
            return f'"{self.name}": np.arange({int(self.min)}, {int(self.max)}, {int(self.step)}),\n'
        return f'"{self.name}": np.arange({self.min}, {self.max}, {self.step}),\n'
