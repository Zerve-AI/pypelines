from .templates.pipeline import PipelineTemplate
from .schemas import HyperParams, NumericalParam, CategoricalParam
from canvas_service.utils.graph_layout import graph_layout
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
        edges = []
        self.parse_config(config)

        #data prep block
        code, imports, requirements = PipelineTemplate()(self.pipeline_params)
        blocks.append({
            'content': code,
            'id': 1
        })

        #model training/testing block
        i = 2
        for model_name, params in self.model_params.items():
            ModelTemplate= self.models[model_name]
            code, model_imports, model_requirements  = ModelTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelTemplate().prefix, params)
                })
            # Split the string at line 20
            code_string_1, code_string_2 = code.split('# Model metrics', maxsplit=1)
            if model_requirements:
                requirements += model_requirements
            if model_imports:
                imports += '\n' + model_imports
            blocks.append({
                'content': code_string_1,
                'id': i
            })
            edges.append((1, i))
            i += 1

        #model metric block
        i = 2+len(self.model_params)
        for model_name, params in self.model_params.items():
            ModelTemplate= self.models[model_name]
            code, model_imports, model_requirements  = ModelTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelTemplate().prefix, params)
                })
            code_string_1, code_string_2 = code.split('# Model metrics', maxsplit=1)
            code_string_2 = '# Model metrics' + code_string_2
            if model_requirements:
                requirements += model_requirements
            if model_imports:
                imports += '\n' + model_imports
            blocks.append({
                'content': code_string_2,
                'id': i
            })
            edges.append((i-len(self.model_params), i))
            i += 1

        #model comparison block    
        i = 2+len(self.model_params)
        j = i+len(self.model_params)
        code_append = ""
        for model_name, params in self.model_params.items():    
            ModelCompTemplate= self.model_comp[model_name]
            code, model_imports, model_requirements  = ModelCompTemplate()({
                **params, 
                **self.shared_model_params, 
                'hyperparams': self.compile_hyperparameters(ModelCompTemplate().prefix, params)
                })
            code_append += code
            edges.append((i,j)) 
            i += 1
        blocks.append({
            'content': code_append,
            'id': j
        }) 
        edges.append((1, j)) 
        
        blocks = graph_layout(blocks, edges, x_offset=x_offset, y_offset=y_offset, reference_node=1)

        # keep unique requirements
        requirements = list(set(requirements))
        # keep unique lines from imports and convert to list
        imports = self.default_imports + '\n' + imports
        imports = list(set(imports.split('\n')))
        

        return blocks, edges, requirements, imports
        