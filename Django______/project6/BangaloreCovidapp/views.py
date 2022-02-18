from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def vijaynagar_corona(request):
    data = '<h1> Corona cases in Vijaynagar Bangalore : 500</h1>'
    return HttpResponse(data)


def btm_corona(request):
    data = '<h1> Corona cases in BTM Bangalore : 700</h1>'
    return HttpResponse(data)


def silkboard_corona(request):
    data = '<h1> Corona cases in Silkboard Bangalore : 900</h1>'
    return HttpResponse(data)
