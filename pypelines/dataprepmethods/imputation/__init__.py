from .MeanMedianImputer import MeanMedianImputer
from .CategoricalImputer import CategoricalImputer
from .ArbitraryNumberImputer import ArbitraryNumberImputer
from .EndTailImputer import EndTailImputer
from .RandomSampleImputer import RandomSampleImputer
from .AddMissingIndicator import AddMissingIndicator


imputation_methods = {
"MeanMedianImputer" : MeanMedianImputer,
"CategoricalImputer" : CategoricalImputer,
"ArbitraryNumberImputer" : ArbitraryNumberImputer,
"EndTailImputer" : EndTailImputer,
"RandomSampleImputer": RandomSampleImputer,
"AddMissingIndicator": AddMissingIndicator
}