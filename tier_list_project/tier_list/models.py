from django.db import models

# Create your models here.

class Departments(models.Model):

    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    price = models.IntegerField(5)
    location = models.IntegerField(5)

    def __str__(self):
        return self.title
