from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display (request):
    return ("<h1>Hola Mundo! secondApp</h1>")

def displaylink(request):
    return ("<a href="https://www.youtube.com/watch?v=f0SyZnnbt-k&ab_channel=LegacyOfKaiser">Youtube</a>")
