from django import forms
# from django.forms.widgets import Widget
from .models import Metrics
class AddMetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields =["metric","value"]
        widgets = {
            'metric':forms.TextInput(attrs={'class':'form_control','id':'metric-input',}),
            'value':forms.NumberInput(attrs={'class':'form_control','id':'metric-value',}),
        }