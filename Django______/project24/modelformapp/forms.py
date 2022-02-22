from modelformapp.models import StudentTable
from django import forms

# class EmployeeForm(forms.Form): --> Form Object
# class StudentTable(forms.ModelForm): --> Model Form Object

class StudentTableForm(forms.Form):
    class Meta:
        model = StudentTable
        fields = ('__all__')
