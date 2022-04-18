from ast import Param
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from myneibourhood.models import NeighbourHood
from .forms import SignupForm, BusinessForm
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            form = SignupForm()
        return render(request,'registration/signup.html',{'form': form})

def hoods(request):
    all_hoods=NeighbourHood.objects.all()
    all_hoods=all_hoods[::-1]
    Params={
        'all_hoods':all_hoods,
    }
    return render(request, 'all_hoods',params)
    

