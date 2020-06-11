from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def blogs(request):
    return render(request, 'blog1.html')
def blogs2(request):
    return render(request, 'blog2.html')
def blogs3(request):
    return render(request, 'blog3.html')


def signout(request):
    auth.logout(request)
    return redirect('/')
