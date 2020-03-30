from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth




def signout(request):
    auth.logout(request)
    return redirect('/')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from givebook.forms import *
from django.http import HttpResponse

from givebook.models import Bookadd
from django.db.models import Q




def getabook(request):
    if request.method == 'GET':
        Books = Bookadd.objects.all()

        return render(request, 'booklist.html',{'Books': Books},)

def requestbook(request):

    availa= request.GET.get('avail')
    avail=Bookadd.objects.get(id = int(availa))
    avail.availability=0
    avail.save()
    Books = Bookadd.objects.all()
    query = request.GET.get('q')
    if query:
        Books = Bookadd.objects.filter(
            Q(bookname__icontains=query) | Q(auther__icontains=query) | Q(language__icontains=query) | Q(
                isbno__icontains=query) | Q(genre__icontains=query))
    return render(request, 'booklist.html', {'Books': Books})

def cancelbook(request):

    availa= request.GET.get('availb')
    avail=Bookadd.objects.get(id = int(availa))
    avail.availability=1
    avail.save()
    Books = Bookadd.objects.all()
    # query = request.GET.get('q')
    # if query:
    #     Books = Bookadd.objects.filter(
    #         Q(bookname__icontains=query) | Q(auther__icontains=query) | Q(language__icontains=query) | Q(
    #             isbno__icontains=query) | Q(genre__icontains=query))
    return render(request, 'booklist.html', {'Books': Books})





def booklist(request):
    Books = Bookadd.objects.all()
    query=request.GET.get('q')
    if query:
        Books=Bookadd.objects.filter(Q(bookname__icontains=query)|Q(auther__icontains=query)|Q(language__icontains=query)|Q(isbno__icontains=query)|Q(genre__icontains=query))
    return render(request, 'booklist.html',{'Books': Books})



