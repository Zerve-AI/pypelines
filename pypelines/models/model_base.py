from ..templates.sklearn_model import SkLearnModelTemplate
from ..templates.sklearn_model_comparison import SkLearnModelComparisonTemplate
from ..templates.pyod_model import PYODModelTemplate
from ..templates.pyod_model_comparison import PYODModelComparisonTemplate
from ..templates.ts_classification_model import TSClassificationModelTemplate
from ..templates.ts_classification_model_comparison import TSClassificationModelComparisonTemplate
from ..templates.ts_regression_model import TSRegressionModelTemplate
from ..templates.ts_regression_model_comparison import TSRegressionModelComparisonTemplate
from ..templates.ts_clustering_model import TSClusteringModelTemplate
from ..templates.ts_clustering_model_comparison import TSClusteringModelComparisonTemplate
from ..templates.clustering_model import ClusteringModelTemplate
from ..templates.clustering_model_comparison import ClusteringModelComparisonTemplate

class SklearnModelBase(SkLearnModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the class with a prefix, model_string, and hyperparameters.
        The super() function calls the __init__ function of its parent (in this case, BaseModel). 
        This allows us to inherit all of BaseModel's functionality while adding our own customizations.
        
        :param self: Represent the instance of the class
        :param prefix: Specify the name of the model
        :param model_string: Specify the model to be used
        :param hyperparameters: Pass the hyperparameters to the model
        :param imports: Import any libraries that are required by the model
        :param model_type: Determine the type of model being used
        :return: The model object
        """
        self.prefix = prefix
        self.model_string = model_string
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
                
        
        :param self: Refer to the instance of the class
        :return: The prefix of the word
        """
        return self.prefix
    

class SklearnModelComparisonBase(SkLearnModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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


class PYODModelBase(PYODModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    


class PYODModelComparisonBase(PYODModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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



class TSClassificationModelBase(TSClassificationModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn','sktime'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    


class TSClassificationModelComparisonBase(TSClassificationModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    

class TSRegressionModelBase(TSRegressionModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn','sktime'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    
class TSRegressionModelComparisonBase(TSRegressionModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    

class TSClusteringModelBase(TSClusteringModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn','sktime'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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

class TSClusteringModelComparisonBase(TSClusteringModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn','sktime'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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



class ClusteringModelBase(ClusteringModelTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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
    


class ClusteringModelComparisonBase(ClusteringModelComparisonTemplate):
    def __init__(self, prefix, model_string, hyperparameters, imports=None,model_type=None):
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
        self.hyperparameters = hyperparameters
        super().__init__(
            requirements=['scikit-learn'],
            default_values={'prefix': prefix, 'model': model_string, 'imports': imports,'model_type': model_type}
        )

    def get_hyperparameters(self):
        """
        The get_hyperparameters function returns a dictionary of hyperparameters.
                The keys are the names of the hyperparameters and the values are their current values.
        
        :param self: Represent the instance of the class
        :return: The hyperparameters of the model
        """
        return self.hyperparameters
    
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