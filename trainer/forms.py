from leadership.models import User
from django import forms

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password')


