from django import forms

class signup_form(forms.Form):
    name = forms.CharField()
    password = forms.PasswordInput()

