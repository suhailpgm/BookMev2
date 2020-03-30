from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    if request.method== 'POST':
        id = request.POST['userid']
        password = request.POST['pass']
        user = auth.authenticate(username=id,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('index')

    else:
        return render(request, 'index.html')



def getbook(request):

        return render(request, 'getbook.html')


