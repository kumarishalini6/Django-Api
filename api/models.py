from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=80)