from django.db import models
# # Create your models here.

class CityName(models.Model):
    city = models.CharField(max_length=100,default=None)
