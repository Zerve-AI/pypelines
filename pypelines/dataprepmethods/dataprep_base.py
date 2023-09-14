from ..templates.dataprep_libraries import DataPrepLibTemplate

class DataPrepBase(DataPrepLibTemplate):
    def __init__(self, prefix, model_string, library, imports=None,model_type=None):
        self.prefix = prefix
        self.model_string = model_string
        self.library = library
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_library(self):
        return self.library
    
    def get_model_string(self):
        return self.model_string
    
    def get_prefix(self):

        return self.prefix
