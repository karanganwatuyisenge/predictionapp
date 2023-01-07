from django import forms
from .models import Patient
from django.forms  import ValidationError

class PatientForm(forms.ModelForm):
    phone=forms.IntegerField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=Patient
        fields=['phone','password1','password2']
    def clean(self):
        errors=[]
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if(password1 != password2):
            errors.append("Password doesn't match")
            