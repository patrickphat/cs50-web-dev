from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, bro..world!")

def coolest_page(request):
    return render(request, "coolest_page/index.html")

def hey_cutie_octopus(request):
    return HttpResponse("Cutie octopus is here")

def hey_patrick(request):
    return HttpResponse("Hey Patrick!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
