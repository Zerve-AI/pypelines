from .DropConstantFeatures import DropConstantFeatures
from .DropCorrelatedFeatures import DropCorrelatedFeatures
from .DropDuplicateFeatures import DropDuplicateFeatures
from .DropHighPSIFeatures import DropHighPSIFeatures
from .ProbeFeatureSelection import ProbeFeatureSelection
from .RecursiveFeatureAddition import RecursiveFeatureAddition
from .RecursiveFeatureElimination import RecursiveFeatureElimination
from .SelectByInformationValue import SelectByInformationValue
from .SelectByShuffling import SelectByShuffling
from .SelectBySingleFeaturePerformance import SelectBySingleFeaturePerformance
from .SelectByTargetMeanPerformance import SelectByTargetMeanPerformance
from .SmartCorrelatedSelection import SmartCorrelatedSelection



featureselection_methods = {
"DropConstantFeatures": DropConstantFeatures,
"DropCorrelatedFeatures": DropCorrelatedFeatures,
"DropDuplicateFeatures": DropDuplicateFeatures,
"DropHighPSIFeatures": DropHighPSIFeatures,
"ProbeFeatureSelection": ProbeFeatureSelection,
"RecursiveFeatureAddition": RecursiveFeatureAddition,
"RecursiveFeatureElimination": RecursiveFeatureElimination,
"SelectByInformationValue": SelectByInformationValue,
"SelectByShuffling": SelectByShuffling,
"SelectBySingleFeaturePerformance": SelectBySingleFeaturePerformance,
"SelectByTargetMeanPerformance": SelectByTargetMeanPerformance,
"SmartCorrelatedSelection": SmartCorrelatedSelection
}