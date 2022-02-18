from django.shortcuts import render
import datetime

# Create your views here.

def rknagar_corona(request):
    data = '<h1> Corona cases in Ramakrishnanagar Mysore : 200</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='MysoreCovidApp/mysore.html', context=dict)


def vijaynagar_corona(request):
    data = '<h1> Corona cases in Vijaynagar Mysore : 100</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='MysoreCovidApp/mysore.html', context=dict)


def kdroad_corona(request):
    data = '<h1> Corona cases in KDroad Mysore : 150</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='MysoreCovidApp/mysore.html', context=dict)
