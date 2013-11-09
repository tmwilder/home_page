#Django
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
