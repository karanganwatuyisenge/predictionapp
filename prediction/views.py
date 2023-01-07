from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,'prediction/index.html')
def signin(request):
    return render(request,'prediction/login.html')
def register(request):
    return render(request,'prediction/register.html')

def patientregistration(request):
    context = {}
    context['form'] = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('patientregistration')
        else:
            context['form'] = form
    return render(request,'prediction/register.html',context)