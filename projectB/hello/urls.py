# projectB/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_hi_from_project_a, name='get_hi_from_project_a'),
]
