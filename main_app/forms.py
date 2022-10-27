from django.forms import ModelForm
from .models import Investing, Symbol

class InvestingForm(ModelForm):
  class Meta:
    model = Investing
    fields = ['date', 'amount']

class SymbolForm(ModelForm):
  class Meta:
    model = Symbol
    fields = ['name','symbol','price',]