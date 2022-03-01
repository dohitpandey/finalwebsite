from django import forms

class Signup(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class':"form-control"}))
