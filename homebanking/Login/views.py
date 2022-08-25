from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.


def login_page(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('home')
		
		else:
			messages.success(request, ('Hubo un error con el login. Por favor, intente nuevamente.'))
			return render(request, 'registration/login.html', {})
	
	else:
		return render(request, 'registration/login.html', {})


@login_required(login_url='login')
def home(request):
	return render(request, 'Login/home.html')


def register(request):
	if request.method == "POST":
		# Inherits UserCreationForms from forms.py, adding some fields
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'El usuario se ha registrado con éxito!')
			return render(request, 'registration/login.html', {})
	
	else:
		form = RegisterUserForm()
	
	return render(request, 'Login/register.html', {'form': form})
