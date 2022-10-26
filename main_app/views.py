from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Symbol, Investment
from main_app.forms import InvestingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


@login_required
def symbols_index(request):
    symbols = Symbol.objects.filter(user=request.user)
    return render(request,'symbols/index.html', {'symbols': symbols})


@login_required
def symbols_detail(request, symbol_id):
  symbol = Symbol.objects.get(id=symbol_id)
  investing_form = InvestingForm()
  investment_symbol_doesnt_have = Investment.objects.exclude(id__in=symbol.investments.all().values_list('id'))

  return render(request, 'symbols/detail.html', {
      'symbol': symbol,
      'investing_form': investing_form,
      'investments':  investment_symbol_doesnt_have,
  })


@login_required
def add_investing(request, symbol_id):
    form = InvestingForm(request.POST)
    if form.is_valid():
        new_investing = form.save(commit=False)
        new_investing.symbol_id = symbol_id
        new_investing.save()
    return redirect('detail', symbol_id=symbol_id)


@login_required
def assoc_investment(request, symbol_id, investment_id):
   Symbol.objects.get(id=symbol_id).investments.add(investment_id)
   return redirect('detail', symbol_id=symbol_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()

            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class SymbolCreate(LoginRequiredMixin, CreateView):
    model = Symbol
    fields = ('name','symbol','price')
    success_url = '/symbols/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)


class SymbolUpdate(LoginRequiredMixin, UpdateView):
    model = Symbol
    fields = ('name','symbol','price')


class SymbolDelete(LoginRequiredMixin, DeleteView):
    model = Symbol
    success_url = '/symbols/'


class SymbolDetail(LoginRequiredMixin, DetailView):
    model = Investment
    template_name = 'symbols/detail.html'

class SymbolList(LoginRequiredMixin, ListView):
    model = Investment
    template_name = 'symbols/index.html'


class InvestmentCreate(LoginRequiredMixin, CreateView):
    model = Investment
    fields = ('name', 'amount')
    success_url = '/investments/'


class InvestmentUpdate(LoginRequiredMixin, UpdateView):
    model = Investment
    fields = '__all__'
    success_url = '/investments/'


class InvestmentDelete(LoginRequiredMixin, DeleteView):
    model = Investment
    success_url = '/investments/'


class InvestmentDetail(LoginRequiredMixin, DetailView):
    model = Investment
    template_name = 'investments/detail.html'


class InvestmentList(LoginRequiredMixin, ListView):
    model = Investment
    template_name = 'investments/index.html'
