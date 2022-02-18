from django.urls import path
from MysoreCovidApp import views as v2

urlpatterns = [

    path('rknagar/', v2.rknagar_corona),
    path('vijaynagar/', v2.vijaynagar_corona),
    path('kdroad/', v2.kdroad_corona),

]