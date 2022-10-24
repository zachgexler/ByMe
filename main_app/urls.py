from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('symbols/', views.symbols_index, name='index'),
    path('symbols/<int:symbols_id>/', views.symbols_detail, name='detail'),
    path('symbols/create/', views.SymbolCreate.as_view(), name='symbols_create'),
    path('symbols/<int:pk>/update',
         views.SymbolUpdate.as_view(), name='symbols_update'),
    path('symbols/<int:pk>/delete',
         views.SymbolDelete.as_view(), name='symbols_delete'),
    path('symbols/<int:symbols_id>/add_investing/',
         views.add_investing, name='add_investing'),
    path('investments/', views.InvestmentList.as_view(), name='investments_index'),
    path('investments/<int:pk>/', views.InvestmentDetail.as_view(),
         name='investments_detail'),
    path('investments/create/', views.InvestmentCreate.as_view(),
         name='investments_create'),
    path('investments/<int:pk>/update/',
         views.InvestmentUpdate.as_view(), name='investments_update'),
    path('investments/<int:pk>/delete/',
         views.InvestmentDelete.as_view(), name='investments_delete'),
    path('investments/<int:investment_id>/assoc_investment/<int:investment_id>/',
         views.assoc_investment, name='assoc_investment'),
]
