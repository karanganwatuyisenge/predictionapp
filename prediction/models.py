from django.db import models
# Create your models here.

class Patient(models.Model):
    phone=models.IntegerField(max_length=100,null=True,blank=False)
    password1=models.CharField(max_length=100,null=True,blank=False)
    password2=models.CharField(max_length=100,null=True,blank=False)

    def __str__(self):
        return self.phone