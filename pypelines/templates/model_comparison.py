from .template_base import AutoPipelineBaseTemplate

template = '''
#comparison metrics - {{prefix}}
{% if model_type == "Regression" %}
{{prefix}}_performance_metrics
{{prefix}}_actual_predicted_plot.show()
{% elif model_type == "Classification" %}
{{prefix}}_performance_metrics
{{prefix}}_roc_auc_plot.show()
{% endif %}
'''

class SkLearnModelComparisonTemplate(AutoPipelineBaseTemplate):
    def __init__(self, requirements=None, required_imports=None, default_values=None):
        super().__init__(
            template=template,
            requirements=requirements,
            required_imports=required_imports,
            default_values=default_values
            )
