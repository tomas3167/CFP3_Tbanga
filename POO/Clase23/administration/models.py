from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# Create your models here.
