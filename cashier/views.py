from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landingpage(request):
        
    return HttpResponse("<h2>Hello, Ini Halaman Saya.</h2> </p> line ke dua")