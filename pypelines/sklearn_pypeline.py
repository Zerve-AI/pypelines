from .templates.pipeline import PipelineTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from .sklearn.classification import models_classification , model_comparison_classification
from .sklearn.regression import models_regression, model_comparison_regression

classification_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
'''

regression_imports = '''
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
'''

class SklearnPipeline:
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance variables that are used by other methods in the class.
        
        
        :param self: Represent the instance of the class
        :return: Nothing
        """
        self.blocks = []
        self.edges = []
        self.models_clf = models_classification
        self.models_reg = models_regression

    def get_settings_classification(self): 
        """
        The get_settings_classification function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing all possible 
        hyperparameters for that model.
        
        :param self: Represent the instance of the class
        :return: A dictionary of hyperparameters for each model
        """
        hyperparameters = {}
        for name, model in self.models_clf.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def get_settings_regression(self): 
        """
        The get_settings_regression function returns a dictionary of hyperparameters for each model.
        The keys are the names of the models and the values are dictionaries containing all 
        hyperparameters for that model.
        
        :param self: Represent the instance of the class
        :return: A dictionary of hyperparameters for each model in the models_reg dictionary
        """
        hyperparameters = {}
        for name, model in self.models_reg.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def parse_config(self, config):
        """
        The parse_config function takes the config dictionary and parses it into a number of different dictionaries.
        The pipeline_params dictionary contains all the parameters that are used in the pipeline, such as dataset and target column.
        The shared_model_params dictionary contains all parameters that are shared between models, such as cross validation settings.
        The model_params dictonary contains all model specific parameters for each selected model.
        
        :param self: Make the function a method of the class
        :param config: Get the model type, selected models and cross validation settings
        :return: A dictionary with the following keys:
        """
        if config['model_type'] == 'classification':
           self.models = models_classification
           self.model_comp = model_comparison_classification
           self.model_param = self.get_settings_classification()
           selected_models = config['selected_models']
           self.metric = 'accuracy_score'
           self.default_imports = classification_imports
        elif config['model_type'] == 'regression':
           self.models = models_regression
           self.model_comp = model_comparison_regression
           self.model_param = self.get_settings_regression()
           selected_models = config['selected_models']
           self.metric = 'mean_squared_error'
           self.default_imports = regression_imports
        self.pipeline_params = {k:v for k,v in config.items() if k in ['dataset', 'target_column']}
        self.shared_model_params = {**{k:v for k,v in config.items() if k in ['cross_validation']}, 'metric':self.metric }
        self.model_params = {k:v for k,v in self.model_param.items() if k in selected_models}
        self.model_comp_params = {k:v for k,v in self.model_param.items() if k in selected_models}

    def compile_hyperparameters(self, model_prefix, params):
        """
        The compile_hyperparameters function takes a model_prefix and params dictionary as input.
        The model_prefix is the name of the model, e.g., 'xgb'. The params dictionary contains two keys:
        'categorical' and 'numerical'. Each key has a list of dictionaries as its value. 
        Each dictionary in this list represents one hyperparameter for that type (categorical or numerical). 
        For example, here's an entry from the categorical list: {'name': 'objective', 'selected': ['reg:linear']}. 
        This means that there is one categorical hyper
        
        :param self: Represent the instance of the class
        :param model_prefix: Identify the model that is being trained
        :param params: Pass in the hyperparameters that you want to tune
        :return: A hyperparams object
        """
        hyperparams = []
        for k, v in params.items():
            for p in v:
                if p.get('checked')==False:
                    continue
                if k=='categorical':
                    if not p['selected']:
                        continue
                    hyperparams.append(CategoricalParam(**{'prefix': model_prefix, 'name': p['name'], 'values': p['selected']}))
                elif k=='numerical':
                    hyperparams.append(NumericalParam(**{'prefix': model_prefix, **p}))
        return HyperParams(**{'params': hyperparams})

    def run(self, config, x_offset=0, y_offset=0):
        """
        The run function is the main function of a block. It takes in a config dictionary, which contains all the parameters that are set by the user in the frontend.
        
        :param self: Represent the instance of the class
        :param config: Pass the configuration of the pipeline to be generated
        :param x_offset: Shift the x position of the block in the canvas
        :param y_offset: Offset the y position of the blocks
        :return: A list of blocks, a list of requirements and a string with imports
        """
        blocks = []
        self.parse_config(config)

        for model_name, params in self.model_params.items():
            i = 1
            code, imports, requirements = PipelineTemplate()(self.pipeline_params)
            imports = self.default_imports + '\n' + imports
            code_append = ""
            code_append += imports
            code_append += code
            ModelTemplate= self.models[model_name]
            code, model_imports, model_requirements  = ModelTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelTemplate().prefix, params)
                })
            if model_requirements:
                requirements += model_requirements
            if model_imports:
                imports += '\n' + model_imports
            code_append += code
            ModelCompTemplate= self.model_comp[model_name]
            code, model_imports, model_requirements  = ModelCompTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelCompTemplate().prefix, params)
                })
            code_append += code
            blocks.append({
                'content': code_append,
                'id': i
            })
            i = i+1
        # keep unique requirements
        requirements = list(set(requirements))
        # keep unique lines from imports and convert to list
        imports = self.default_imports + '\n' + imports
        #imports = list(set(imports.split('\n')))
        return blocks, requirements, imports
        