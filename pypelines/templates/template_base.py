from jinja2 import Template



class AutoPipelineBaseTemplate:
    def __init__(self, template, requirements=None, required_imports=None, default_values=None):
        self.requirements = requirements
        self.required_imports = required_imports
        self.default_values = {} if not default_values else default_values
        self.template = template
    
    def __call__(self, values):
        print(self.default_values)
        code =  Template(self.template).render(**{**self.default_values, **values})
        return code, self.required_imports, self.requirements