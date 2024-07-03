from django.db import models

class Administration(models.Model):
    name = models.CharField(max_length=250)
    administration = models.ForeignKey

    def __str__(self):
        return self.name

# Create your models here.
