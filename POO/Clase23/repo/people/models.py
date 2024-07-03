from django.db import models

class People(models.Model):
    name = models.CharField(max_length=250)
    subname = models.CharField(max_length=250)
    dni = models.CharField(max_length=8)
    age = models.IntegerField
    administration = models.ForeignKey


# Create your models here.
