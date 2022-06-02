
from django.contrib import admin
from django.urls import path
from Bolano import views

urlpatterns = [
    path("admin/", admin.site.urls,name='admin'),
    path("", views.index, name='Bolano'),
    path("about", views.about, name='about'),
    path("service", views.service, name='service'),
    path("contact", views.contact, name='contact'),

    
]
