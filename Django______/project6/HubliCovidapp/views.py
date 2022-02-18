from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def vidyanagar_corona(request):
    data = '<h1> Corona cases in Vidyanagar Hubli : 50</h1>'
    return HttpResponse(data)


def ashwininagar_corona(request):
    data = '<h1> Corona cases in Ashwininagar Hubli : 70</h1>'
    return HttpResponse(data)


def gokulroad_corona(request):
    data = '<h1> Corona cases in Gokulroad Hubli : 80</h1>'
    return HttpResponse(data)
