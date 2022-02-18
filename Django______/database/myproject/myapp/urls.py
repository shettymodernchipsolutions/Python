from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage),
    path('register', addstudent, name='ad'),
    path('retrieve', search, name='rd'),
    path('update', update, name='ud'),
]