from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Symbol, Investment
from main_app.forms import InvestingForm, SymbolForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
User = get_user_model()

def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


# @login_required
# def symbols_index(request):
#     symbols = Symbol.objects.filter(user=request.user)
#     return render(request,'symbols/index.html', {'symbols': symbols})


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

# @login_required
# def add_symbol(request):
#     return render(request, 'symbols/createSymbol.html')
@login_required
def add_investing(request, symbol_id):
   form = InvestingForm(request.POST)
   if form.is_valid():
       # new_investing = form.save(commit=False)
       # new_investing.symbol_id = symbol_id
       # new_investing.save()
    return redirect('detail', symbol_id=symbol_id)


@login_required
def assoc_investment(request, symbol_id, investment_id):
   #ymbol.objects.get(id=symbol_id).investments.add(investment_id)
   return redirect('detail', symbol_id=symbol_id)



class CreateSymbol(CreateView):
    model = Symbol
    fields = '__all__'
    template_name = "symbols/createSymbol.html"


    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class SymbolUpdate(UpdateView):
    model = Symbol
    fields = ('name','symbol','price')
    template_name = 'symbols_update.html'

class SymbolDelete(DeleteView):
    model = Symbol
    success_url = reverse_lazy('home')
    template_name = 'symbols_delete.html'


class SymbolDetail(LoginRequiredMixin, DetailView):
    model = Investment
    template_name = 'symbols/detail.html'

class SymbolList(ListView):
    model = Symbol
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
    template_name = 'investments/delete_investment.html'


class InvestmentDetail(LoginRequiredMixin, DetailView):
    model = Investment
    template_name = 'investments/detail.html'


class InvestmentList(LoginRequiredMixin, ListView):
    model = Investment
    template_name = 'investments/index.html'
