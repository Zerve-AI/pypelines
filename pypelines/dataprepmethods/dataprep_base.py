from ..templates.dataprep_libraries import DataPrepLibTemplate
from ..templates.pyod_model import PYODModelTemplate



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
    


class PYODModelBase(PYODModelTemplate):
    def __init__(self, prefix, model_string, library, imports=None,model_type=None):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the class with a prefix, model_string, and hyperparameters.
        The super() function calls the __init__ function of its parent (in this case, BaseModel). 
        This allows us to inherit all of BaseModel's functionality while adding our own customizations.
        
        :param self: Represent the instance of the class
        :param prefix: Identify the model
        :param model_string: Create the model object
        :param hyperparameters: Pass in the hyperparameters of the model
        :param imports: Import any additional libraries that are required by the model
        :param model_type: Determine the type of model to be used
        :return: The super() method
        """
        self.prefix = prefix
        self.model_string = model_string
        self.library = library
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_library(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.library
    
    def get_model_string(self):
        """
        The get_model_string function returns the model string of a given instance of the Model class.
            
        
        :param self: Represent the instance of the class
        :return: The model_string attribute of the object
        """
        return self.model_string
    
    def get_prefix(self):
        """
        The get_prefix function returns the prefix of the command.
                
        
        :param self: Refer to the class instance itself
        :return: The prefix of a word
        """
        return self.prefix
    
