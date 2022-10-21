from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('ByMe')

def about(request):
  return render(request, 'about.html')