                             #givebook backend codes
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
def bookupload(request):

	if request.method == 'POST':
		form = Givebookform(request.POST, request.FILES)

		if form.is_valid():
			instance=form.save(commit=False)
			instance.user=request.user
			instance.save()
			return redirect('success')
	else:
		form = Givebookform()


	return render(request, 'givebook.html', {'form' : form})

def success(request):
	return redirect('getstarted')