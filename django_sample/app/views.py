from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *


def register(request):
	form = Register(request.POST)
	if request.method == 'POST':
		form=Register(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Successfully registered')
			return redirect('register')

	return render(request,'register.html',locals())


def display(request):
	person_list=Details.objects.order_by('-pk')
	return render(request,'details.html',locals())

