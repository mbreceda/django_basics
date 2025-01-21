from django.urls import path

from . import views

urlpatterns = [
    path('add', views.inventory, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
]