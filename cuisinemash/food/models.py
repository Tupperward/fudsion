from django.db import models
from django_random_queryset import RandomManager

# Create your models here.
class Dish(models.Model):
    dishName = models.CharField(max_length=140)
    description = models.CharField(max_length=280)
    cuisine = models.CharField(max_length=48)
    #likes = models.IntegerField()
    def __str__(self):
        return self.dishName

