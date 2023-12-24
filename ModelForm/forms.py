from django import forms
from .models import Modelss

class ExploreModelForm(forms.ModelForm):
    class Meta:
        model = Modelss
        fields = '__all__'