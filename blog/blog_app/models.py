from django.db import models

# Create your models here.
class Page(models.Model):
    content = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
