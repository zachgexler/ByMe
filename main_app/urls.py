from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('symbols/', views.symbols_index, name='index'),
    path('symbols/<int:symbols_id>/', views.symbols_detail, name='detail'),
    path('symbols/create/', views.SymbolCreate.as_view(), name='symbols_create'),
    path('symbols/<int:pk>/update', views.SymbolUpdate.as_view(), name='symbols_update'),
    path('symbols/<int:pk>/delete', views.SymbolDelete.as_view(), name='symbols_delete'),
    path('symbols/<int:symbols_id>/add_invetment/', views.add_investment, name='add_investment'),
]