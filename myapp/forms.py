from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
   name = forms.CharField(
      widget = forms.TextInput(attrs={'class': 'form-control'}))
   image = forms.FileField(
      widget = forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}))
   description = forms.CharField(
      widget = forms.Textarea(attrs={'class': 'form-control'}) )

   class Meta:
      model = Image
      fields = ('name', 'image', 'description', )
