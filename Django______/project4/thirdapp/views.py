from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def third_app(request):
    data = '<h1>Thanks for connecting to Third Application</h1>'
    return HttpResponse(data)