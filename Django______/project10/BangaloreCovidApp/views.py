from django.shortcuts import render
import datetime


# Create your views here.

def vijaynagar_corona(request):
    data = '<h1> Corona cases in Vijaynagar Bangalore : 500</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='BangaloreCovidApp/bangalore.html', context=dict)


def btm_corona(request):
    data = '<h1> Corona cases in BTM Bangalore : 700</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='BangaloreCovidApp/bangalore.html', context=dict)


def silkboard_corona(request):
    data = '<h1> Corona cases in Silkboard Bangalore : 900</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='BangaloreCovidApp/bangalore.html', context=dict)
