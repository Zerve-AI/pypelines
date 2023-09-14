from .LogTransformer import LogTransformer
from .LogCpTransformer import LogCpTransformer
from .ArcsinTransformer import ArcsinTransformer
from .BoxCoxTransformer import BoxCoxTransformer
from .PowerTransformer import PowerTransformer
from .ReciprocalTransformer import ReciprocalTransformer
from .YeoJohnsonTransformer import YeoJohnsonTransformer



transformer_methods = {
"LogTransformer": LogTransformer,
"LogCpTransformer":  LogCpTransformer,
"ArcsinTransformer":  ArcsinTransformer,
"BoxCoxTransformer": BoxCoxTransformer,
"PowerTransformer":  PowerTransformer,
"ReciprocalTransformer":  ReciprocalTransformer,
"YeoJohnsonTransformer":  YeoJohnsonTransformer
}