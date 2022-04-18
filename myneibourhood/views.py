import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignupForm, BusinessForm


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
            loging(request, user)
            return redirect('index')
        else:
            form = SignupForm()
        return render(request,'registration/signup.html',{'form': form})

