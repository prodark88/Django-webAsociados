from django.urls import path
from services import views


urlpatterns = [
    path('', views.services , name='services'),
    path('detail/<int:id>/', views.services_by_especialidad, name='services_by_especialidad'),
]