from django.db import models
from django.urls import reverse
# Create your models here.

class Investment(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField(max_length=50)

def get_absolute_url(self):
    return reverse('investments_detail', kwargs={'pk': self.id})

class Symbol(models.Model):
  name = models.CharField(max_length=100)
  symbol = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  price = models.FloatField()
  investment = models.ManyToManyField(Investment)

def __str__(self):
    return self.name