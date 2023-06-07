from pydantic import BaseModel
from typing import List, Union


class ConstantParam(BaseModel):
    prefix: str
    name: str
    value: float

    def __repr__(self):
        return f'{self.name}: {self.value},\n'

    def __str__(self):
        return f'{self.name}: {self.value},\n'
    
class ConstantParamAD(BaseModel):
    name: str
    value: float

    def __repr__(self):
        return f'{self.name}: {self.value},\n'

    def __str__(self):
        return f'{self.name}: {self.value},\n'
