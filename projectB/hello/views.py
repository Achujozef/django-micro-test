# projectB/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse

def get_hi_from_project_a(request):
    response = requests.get("http://localhost:8000/hello/hi/")
    if response.status_code == 200:
        return HttpResponse(response.text)
    else:
        return HttpResponse("Failed to get 'Hi' from Project A")
