from django.urls import path
from .views import InventoryView, dashboard

urlpatterns = [
    path('add/', InventoryView.as_view(), name='add'),
    path('dashboard/', dashboard, name='dashboard'),
]
