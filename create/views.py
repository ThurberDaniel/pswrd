from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'create/home.html', {'passwrd':'0987uyhjkiuy765ret6y78*&^%$'})

def password(request):
    lowCharacters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        lowCharacters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        lowCharacters.extend(list('?>*&^%$#@!+},'))
    if request.GET.get('numbers'):
        lowCharacters.extend(list('1234567890'))

    length = int(request.GET.get('length', 7))
    pswrd = ''
    for z in range(length):
        pswrd += random.choice(lowCharacters)
    return render(request, 'create/password.html',{'password':pswrd})

