from django.forms import ModelForm
from .models import Investing

class InvestingForm(ModelForm):
  class Meta:
    model = Investing
    fields = ['date', 'amount']