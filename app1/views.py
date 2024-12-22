from django.shortcuts import render, redirect
from .models import qpage, ppage, song
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')

def hb(request):
    return render(request,'hb.html',{'pages':qpage.objects.all()})

def sp(request):
    return render(request,'sp.html',{'pages':ppage.objects.all()})

def s(request):
    return render(request,'s.html',{'songs':song.objects.all()})

def login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['pass'])
        if user != None:
            login(request)
            return redirect('menu')
    return render(request,'login.html')
