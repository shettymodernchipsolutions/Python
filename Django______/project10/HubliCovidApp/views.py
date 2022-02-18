from django.shortcuts import render
import datetime


# Create your views here.

def vidyanagar_corona(request):
    data = '<h1> Corona cases in Vidyanagar Hubli : 50</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='HubliCovidApp/hubli.html', context=dict)


def ashwininagar_corona(request):
    data = '<h1> Corona cases in Ashwininagar Hubli : 70</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='HubliCovidApp/hubli.html', context=dict)


def gokulroad_corona(request):
    data = '<h1> Corona cases in Gokulroad Hubli : 80</h1>'
    server_time = datetime.datetime.now()

    dict = {'data': data, 'server_time': server_time}

    return render(request=request, template_name='HubliCovidApp/hubli.html', context=dict)
