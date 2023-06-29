from pydantic import BaseModel
from typing import List, Union


class CategoricalParam(BaseModel):
    prefix: str
    name: str
    values: list

    def __repr__(self):
        return f'"{self.prefix}__{self.name}": {self.values},\n'
    
    def __str__(self):
        return f'"{self.prefix}__{self.name}": {self.values},\n'
    

class CategoricalParamAD(BaseModel):
    name: str
    values: list

    def __repr__(self):
        return f'"{self.name}": {self.values},\n'
    
    def __str__(self):
        return f'"{self.name}": {self.values},\n'
    

class CategoricalParamTSClassification(BaseModel):
    name: str
    values: list

    def __repr__(self):
        return f'"{self.name}": {self.values},\n'
    
    def __str__(self):
        return f'"{self.name}": {self.values},\n'