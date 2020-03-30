from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def getstarted(request):
    return render(request, 'getstarted.html')


def signout(request):
    auth.logout(request)
    return redirect('/')
