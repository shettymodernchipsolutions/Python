from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def rknagar_corona(request):
    data = '<h1> Corona cases in Ramakrishnanagar Mysore : 200</h1>'
    return HttpResponse(data)


def vijaynagar_corona(request):
    data = '<h1> Corona cases in Vijaynagar Mysore : 100</h1>'
    return HttpResponse(data)


def kdroad_corona(request):
    data = '<h1> Corona cases in KDroad Mysore : 150</h1>'
    return HttpResponse(data)
