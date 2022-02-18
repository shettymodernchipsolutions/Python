from django import forms

class Student(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()