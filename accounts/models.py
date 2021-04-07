from django.db import models

# Create your models here.
class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10, unique=True)
    status = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)