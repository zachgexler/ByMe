from django.db import models

# Create your models here.

class Symbol(models.Model):
  name = models.CharField(max_length=100)
  symbol = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  price = models.FloatField()
  investment = models.ManyToManyField(Investment)

def __str__(self):
    return self.name