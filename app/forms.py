from cProfile import label
from statistics import mode
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        label = ('photo:', '')
