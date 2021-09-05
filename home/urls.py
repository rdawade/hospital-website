from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index),
    path("about",views.about),
    path("services",views.services),
    path("contact",views.contact),
    path("medicine",views.medicine),
    path("doctor",views.doctor),
    path("patient",views.patient),
    path("online",views.online),
    path("appointment",views.appointment),
    path("emergency",views.emergency),
    path("ambulance",views.ambulance)
]
