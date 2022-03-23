from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'create/home.html')

def names(request):
    return HttpResponse("TESTING")

