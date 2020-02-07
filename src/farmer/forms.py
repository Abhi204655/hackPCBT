from django import forms
from .models import Land
class LandForm(forms.Form):
    class Meta:
        model = Land
        fields = '__all__'