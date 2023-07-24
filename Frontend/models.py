from django.db import models


# Create your models here.
class cartDB(models.Model):
    Pname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)


class cartdetails(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    PostalCode = models.IntegerField(null=True, blank=True)
    PhoneNo = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)


class customerdetails(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm_password = models.CharField(max_length=100, null=True, blank=True)
