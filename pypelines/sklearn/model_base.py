from ..templates.sklearn_model import SkLearnModelTemplate
from ..templates.model_comparison import SkLearnModelComparisonTemplate


class SklearnModelBase(SkLearnModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
        self.prefix = prefix
        self.model_string = model_string
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        return self.hyperparameters
    
    def get_model_string(self):
        return self.model_string
    
    def get_prefix(self):
        return self.prefix
    

class SklearnModelComparisonBase(SkLearnModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
        self.prefix = prefix
        self.model_string = model_string
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        return self.hyperparameters
    
    def get_model_string(self):
        return self.model_string
    
    def get_prefix(self):
        return self.prefix