from .ExpandingWindowFeatures import ExpandingWindowFeatures
from .WindowFeatures import WindowFeatures
from .LagFeatures import LagFeatures



forecasting_methods = {
"LagFeatures": LagFeatures,
"DatetimeFeatures" : ExpandingWindowFeatures,
"DatetimeSubtraction" : WindowFeatures
}