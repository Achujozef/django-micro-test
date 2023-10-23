# projectA/hello/views.py
from django.http import HttpResponse

def say_hi(request):
    return HttpResponse("Hi from Project Achu Jozef S L!")
