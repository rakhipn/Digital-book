from django.db import models


# Create your models here.
class categorydb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)


class productdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Author = models.CharField(max_length=100, null=True, blank=True)
    Language = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Pages = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=900, null=True, blank=True)
