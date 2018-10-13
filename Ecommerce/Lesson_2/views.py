# view.py is in the same folder as urls.py
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("<h1>Hello World</h1>")
