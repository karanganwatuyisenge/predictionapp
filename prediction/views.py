from django.shortcuts import  render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'prediction/index.html')

def signin(request):
    return render(request,'prediction/login.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(user.is_staff)
				if user.is_staff == False:
					return redirect("inner")
				else:
					return redirect("registration")

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="prediction/login.html", context={"login_form":form})

def registration(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('login')
        else:
            context['form'] = form
    return render(request,'prediction/register1.html',context)

def inner(request):
    return render(request,'prediction/inner-page.html')