
from django.urls import path
from publications import views


urlpatterns = [
    path('', views.publications, name='publications'),
    path('detail/<int:publication_id>/', views.publication_detail , name='publication_detail'),
]
