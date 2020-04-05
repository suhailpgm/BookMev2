from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from givebook.forms import *
from django.http import HttpResponse
from givebook.models import Bookadd
from django.db.models import Q
from status.models import Chat
from .forms import *






def myrequests(request):
    if request.method == 'GET':
        Books = Bookadd.objects.all()
        # Books = Bookadd.objects.filter(Q(reqid=request.user.id))
        args = {}
        MSG = Chat.objects.all()
        args['MSG'] = MSG
        args['Books'] = Books

        return render(request, 'myrequests.html', args)



def requests(request):
    if request.method == 'GET':
        Books = Bookadd.objects.all()
        # Books = Bookadd.objects.filter(Q(reqid=request.user.id))
        return render(request, 'requests.html',{'Books': Books},)



def chats(request):
    availbb = request.POST.get('chatpassreciever')
    availcc = request.POST.get('chatpassrecieverid')
    availdd = request.POST.get('chatpassmessage')
    availaa=request.user
    form = chatform(request.POST, request.FILES)
    print("1111111111111111111")
    print(availaa)
    print(availbb)
    print(availcc)
    print(availdd)
    avail=Chat.objects.create(sender=availaa,reciever=availbb,recieverid=availcc,message=availdd)
    avail.save()
    bvail = Chat.objects.latest('id')
    rid = bvail.recieverid
    rname=bvail.reciever
    args = {}
    MSG = Chat.objects.all()
    args['form'] = form
    args['MSG'] = MSG
    args['rid'] = rid
    args['rname'] = rname
    return render(request, 'chatbody.html', args)


def chatsend(request):

    if request.method == 'POST':

        form = chatform(request.POST, request.FILES)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.sender=request.user
            bvail=Chat.objects.latest('id')
            instance.recieverid=bvail.recieverid
            rid = bvail.recieverid
            rname = bvail.reciever
            instance.reciever=bvail.reciever
            instance.save()
            args = {}

            MSG = Chat.objects.all()
            args['form'] = form
            args['MSG'] = MSG
            args['rid'] =rid
            args['rname'] = rname

            return render(request, 'chatbody.html', args)
    else:
        form = chatform()

    args = {}

    MSG = Chat.objects.all()
    rid = bvail.recieverid
    rname = bvail.reciever
    args['form'] = form
    args['MSG'] = MSG

    return render(request, 'chatbody.html', args)
