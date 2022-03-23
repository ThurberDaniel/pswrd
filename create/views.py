from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'create/home.html', {'password':'0987uyhjkiuy765ret6y78*&^%$'})

def password(request):
    return render(request, 'create/password.html')

