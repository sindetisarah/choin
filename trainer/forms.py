from leadership.models import User
from django import forms

from trainer.models import Trainer

class TrainerUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

class TrainerUserProfileForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = (
            'gender',
            'image',
        )
