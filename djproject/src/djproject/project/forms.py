from django import forms

class MyPhotoForm(forms.Form):
    title = forms.CharField()
    image = forms.ImageField()