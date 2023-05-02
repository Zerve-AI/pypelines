from jinja2 import Template



class AutoPipelineBaseTemplate:
    def __init__(self, template, requirements=None, required_imports=None, default_values=None):
        """
        The __init__ function is the constructor for a class. It is called when an object of that class
        is instantiated, and it sets up the attributes of that object. In this case, we are setting up 
        the attributes for our template_class objects.
        
        :param self: Represent the instance of the class
        :param template: Define the template of the code that will be generated
        :param requirements: Specify the requirements of the template
        :param required_imports: Import any modules that are required by the template
        :param default_values: Set default values for the parameters in the template
        :return: Nothing
        """
        self.requirements = requirements
        self.required_imports = required_imports
        self.default_values = {} if not default_values else default_values
        self.template = template
    
    def __call__(self, values):
        """
        The __call__ function is called when the class instance is called.
        It takes a dictionary of values and returns a tuple of (code, imports, requirements).
        The code returned should be valid Python code that can be executed to produce the desired output.
        The imports are any modules that need to be imported in order for the code to run properly.  These will automatically get added at runtime by our system.  The requirements are any additional packages that need to be installed on top of what we already have installed in our environment.
        
        :param self: Access the attributes and methods of the class
        :param values: Pass the values that are used in the template
        :return: A tuple of three elements:
        """
        #print(self.default_values)
        code =  Template(self.template).render(**{**self.default_values, **values})
        return code, self.required_imports, self.requirements