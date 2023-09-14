from .CountFrequencyEncoder import CountFrequencyEncoder
from .DecisionTreeEncoder import DecisionTreeEncoder
from .MeanEncoder import MeanEncoder
from .OneHotEncoder import OneHotEncoder
from .OrdinalEncoder import OrdinalEncoder
from .RareLabelEncoder import RareLabelEncoder
from .WoEEncoder import WoEEncoder
from .StringSimilarityEncoder import StringSimilarityEncoder


encoding_methods = {
"CountFrequencyEncoder" : CountFrequencyEncoder,
"DecisionTreeEncoder" : DecisionTreeEncoder,
"MeanEncoder" : MeanEncoder,
"OneHotEncoder" : OneHotEncoder,
"OrdinalEncoder" : OrdinalEncoder,
"RareLabelEncoder" : RareLabelEncoder,
"WoEEncoder" : WoEEncoder,
"StringSimilarityEncoder" : StringSimilarityEncoder
}