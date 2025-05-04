from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sekretarz/', views.sekretarz_view, name='sekretarz_view'),
    path('rada/', views.rada_view, name='rada_view'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('no-permission/', lambda request: render(request, 'no_permission.html'), name='no_permission'),
    path('dodaj-przewod/', views.dodaj_przewod, name='dodaj_przewod'),

]

def home(request):
    return render(request, 'home.html')