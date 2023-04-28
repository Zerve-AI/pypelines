from .templates.pipeline import PipelineTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
#from canvas_service.utils.graph_layout import graph_layout
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
        self.blocks = []
        self.edges = []
        self.models_clf = models_classification
        self.models_reg = models_regression

    def get_settings_classification(self): 
        hyperparameters = {}
        for name, model in self.models_clf.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def get_settings_regression(self): 
        hyperparameters = {}
        for name, model in self.models_reg.items():
            hyperparameters[name] = model().get_hyperparameters()
        return hyperparameters
    
    def parse_config(self, config):
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
        blocks = []
        self.parse_config(config)

        for model_name, params in self.model_params.items():
            i = 1
            code, imports, requirements = PipelineTemplate()(self.pipeline_params)
            code_append = ""
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
        imports = list(set(imports.split('\n')))
        

        return blocks, requirements, imports
        