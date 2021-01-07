from django import forms
from .models import InfoPage, Picture
from cloudinary.forms import CloudinaryFileField

class InfoForm(forms.ModelForm):
    class Meta:
        model = InfoPage
        fields = [
            "info",
            "tel"
        ]

class PhotoForm(forms.ModelForm):
  class Meta:
      model = Picture
      fields = [
        "image"
      ]
