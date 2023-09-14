from .EqualFrequencyDiscretiser import EqualFrequencyDiscretiser
from .ArbitraryDiscretiser import ArbitraryDiscretiser
from .DecisionTreeDiscretiser import DecisionTreeDiscretiser
from .EqualWidthDiscretiser import EqualWidthDiscretiser
from .GeometricWidthDiscretiser import GeometricWidthDiscretiser




discretisation_methods = {
"EqualFrequencyDiscretiser" : EqualFrequencyDiscretiser,
"ArbitraryDiscretiser" : ArbitraryDiscretiser,
"DecisionTreeDiscretiser" : DecisionTreeDiscretiser,
"EqualWidthDiscretiser" : EqualWidthDiscretiser,
"GeometricWidthDiscretiser" : GeometricWidthDiscretiser,
}