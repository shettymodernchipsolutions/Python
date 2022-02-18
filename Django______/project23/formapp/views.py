from django.shortcuts import render

from formapp.forms import EmployeeForm


# Create your views here.

def home_page(request):
    return render(request=request, template_name='formapp/homepage.html')


def thank_you(request):
    return render(request=request, template_name='formapp/thankyou.html')


def register_data(request):
    form = EmployeeForm()
    my_dict = {'form': form}

    if request.method == 'POST':
        form = EmployeeForm()
        my_dict = {'form': form}

        if form.is_valid():
            print('The Details Entered by Employee: \n\n')
            print('NAME: ', form.cleaned_data['name'])
            print('ADDRESS: ', form.cleaned_data['address'])
            print('SALARY: ', form.cleaned_data['salary'])
            print('MAIL ID: ', form.cleaned_data['mail_id'])
            print('PHONE NUMBER: ', form.cleaned_data['phone_number'])

            return thank_you(request)

    return render(request=request, template_name='formapp/register.html', context=my_dict)
