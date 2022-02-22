from django.shortcuts import render
from modelformapp.models import StudentTable
from modelformapp.forms import StudentTableForm

# Create your views here.

def student_data(request):
    # if request.method == 'GET':
    #     form = StudentTableForm()
    #     my_dict = {'form':form}
    #     return render(request=request, template_name='modelformapp/display.html', context=my_dict)

    form = StudentTableForm()
    my_dict = {'form': form}

    if request.method == 'POST':
        data_form = StudentTableForm(request.POST)
        if data_form.is_valid():
            data_form.save(commit=True)
            print('Data is successfully stored in the database.\n\n')

            print('Data entered by the End user:')
            print(data_form.cleaned_data)
            print(type(data_form.cleaned_data))
            print('Name of the Student:', data_form.cleaned_data['name'])
            print('DOB of the Student:', data_form.cleaned_data['dob'])
            print('MAIL ID of the Student:', data_form.cleaned_data['mail_id'])
            print('PHONE NUMBER of the Student:', data_form.cleaned_data['phone_number'])
            print('BRANCH of the Student:', data_form.cleaned_data['branch'])




    return render(request=request, template_name='modelformapp/display.html', context=my_dict)