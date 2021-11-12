from django import forms
from django.forms import fields
from .models import Metrics, RedeemableItem

class AddMetricsForm(forms.ModelForm):
    class Meta:
        model = Metrics
        fields =["metric","value"]
        widgets = {
            'metric':forms.TextInput(attrs={'class':'form_control','id':'metric-input',}),
            'value':forms.NumberInput(attrs={'class':'form_control','id':'metric-value',}),
        }

        
class RewardItemForm(forms.ModelForm):
    class Meta:
        model=RedeemableItem
        fields=["image", "item_name","item_value","quantity"]
