from django.contrib import admin
from django.urls import path, include
from Bolano import views

urlpatterns = [
    path('',views.index,name="Bolano"),
    path('login',views.loginUser,name="login"),
     path('logout',views.logout,name="logout"),
]