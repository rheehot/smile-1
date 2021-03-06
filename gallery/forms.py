from django import forms
from .models import Photo, Selfie

class PhotoPost(forms.ModelForm):
    class Meta:
        model = Photo
        # fields = ['owner', 'image']
        fields = ['image']


class SelfiePost(forms.ModelForm):
    class Meta:
        model = Selfie
        fields = ['image']


class PhotosPost(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})) 
    class Meta:
        model = Photo
        fields = ['image']