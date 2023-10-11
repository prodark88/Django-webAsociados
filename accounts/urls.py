from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.viewPosition , name='viewPosition'),
    path('staff', views.staff , name='staff'),
    path('enterprise', views.enterprise , name='enterprise'),
]
