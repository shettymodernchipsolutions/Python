from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def second_app(request):
    data = '<h1>Thanks for connecting to Second Application</h1>'
    return HttpResponse(data)