from django import forms
from .models import FoodFitnessModel
# made the Foregin key for practice and practice with exclusion.

class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model = FoodFitnessModel
        exclude = ['identificationKey']
