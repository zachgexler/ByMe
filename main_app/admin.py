from django.contrib import admin
from main_app.models import Symbol
from .models import Symbol, Investing

admin.site.register(Symbol)
admin.site.register(Investing)