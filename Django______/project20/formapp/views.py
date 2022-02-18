from django.shortcuts import render
from formapp.forms import Student


# Create your views here.

def student_data(request):
    form_data = Student()
    print(form_data)
    print(type(form_data))  # --> <class 'formapp.forms.Student'>

    my_dict = {'form_data': form_data}
    print(my_dict)  # --> {'form_data': <Student bound=False, valid=False, fields=(name;age;address)>}
    print(type(my_dict))  # --> <class 'dict'>

    return render(request=request, template_name='formapp/display.html', context=my_dict)
