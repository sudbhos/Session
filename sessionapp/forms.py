from django import forms


class namei(forms.Form):
    name=forms.CharField(max_length=100)

class surnamei(forms.Form):
    surname=forms.CharField(max_length=100)

class cityi(forms.Form):
    city=forms.CharField(max_length=100)
