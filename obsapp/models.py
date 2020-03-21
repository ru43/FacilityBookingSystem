from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user=models.OneToOneField(User,null=True , on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.name

class Facility(models.Model):
    fname=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.fname

class Book(models.Model):
    customer=models.ForeignKey(Customer , null=True, on_delete=models.SET_NULL)
    facility=models.ForeignKey(Facility,null=True, on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        template='{0.customer} booked {0.facility}'
        return template.format(self)
