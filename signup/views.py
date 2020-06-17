                                                   #user registration

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def signuppage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['second_name']
        Username = request.POST['Username']
        password1 = request.POST['pass']
        password2 = request.POST['cpass']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username already taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=Username,password=password1,email=email,first_name=first_name,last_name=last_name )
                user.save();
                messages.info(request,'User created')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'contact.html')

def signout(request):
      auth.logout(request)
      return redirect('/')

def about(request):
    return render(request, 'about.html')