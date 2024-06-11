from django.contrib.auth import forms

class signup_form(forms.Form):
    name = forms.CharField()