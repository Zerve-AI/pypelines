from .ArbitraryOutlierCapper import ArbitraryCapperOutlier
from .OutlierTrimmer import OutlierTrimmer
from .Winsorizer import WinsorizerOutlier



outlier_methods = {
    'ArbitraryCapper': ArbitraryCapperOutlier,
    'Outlier Trimmer': OutlierTrimmer,
    'Winsorizer': WinsorizerOutlier,
}