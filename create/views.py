from django.shortcuts import render
from django.http import HttpResponse
import random



def home(request):
    return render(request, 'create/home.html')
def about(request):
    return render(request, 'create/about.html')


def password(request):
    lowCharacters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        lowCharacters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        lowCharacters.extend(list('?>*&^%$#@!+},==++{?~!!'))
    if request.GET.get('numbers'):
        lowCharacters.extend(list('1234567890'))
    length = int(request.GET.get('length', 7))
    pswrd = ''
    for z in range(length):
        pswrd += random.choice(lowCharacters)
    return render(request, 'create/password.html',{'password':pswrd})

