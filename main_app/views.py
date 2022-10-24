from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Symbol, Investment, Investing
from .forms import InvestingForm

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def symbols_detail(request, symbol_id):
  symbols = Symbol.objects.get(id=symbol_id)
  investing_form = InvestingForm()
  investments_symbol_doesnt_have = Investment.objects.exclude(id__in = symbols.investments.all().values_list('id'))

def assoc_investment(request, symbol_id, investment_id):
   Investment.objects.get(id=symbol_id).investments.add(investment_id)
   return redirect('detail', symbol_id=symbol_id)

class SymbolCreate(CreateView):
    model = Symbol
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/symbols'

class SymbolUpdate(UpdateView):
  model = Symbol
  fields = ['name', 'description', 'price', 'investment']

class SymbolDelete(DeleteView):
  model = Symbol
  success_url = '/symbols'

class SymbolCreate(CreateView):
    model = Symbol
    fields = ('name','description', 'price', 'investment')

class InvestmentUpdate(UpdateView):
    model = Investment
    fields = ('symbol', 'price')

class InvestmentDelete(DeleteView):
    model = Investment
    success_url = '/investments/'

class InvestmentDetail(DetailView):
    model = Investment
    template_name = 'investments/detail.html'

class InvestmentList(ListView):
    model = Investment
    template_name = 'investments/index.html'

  