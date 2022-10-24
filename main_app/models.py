from django.db import models
from django.urls import reverse

INVESTMENTS = (
    ('C', 'Credit'),
    ('D', 'Debit'),
)


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


def get_absolute_url(self):
    return reverse('detail', kwargs={'symbol_id': self.id})


class Investing(models.Model):
    date = models.DateField("Investing Date")
    amount = models.IntegerField(
        max_length=1000000,
        default=INVESTMENTS[0][0])
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.get_investing_display()} on {self.date}"


class Meta:
    ordering = ['-date']
