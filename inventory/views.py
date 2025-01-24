from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django import forms

from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'description', 'color', 'doors', 'lot_number']

class InventoryView(View, LoginRequiredMixin):
    def get(self, request):
        form = VehicleForm()
        return render(request, 'inventory/add.html', {'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user_id = request.user.id
            vehicle.save()
            messages.success(request, 'Vehicle added')
            return redirect('dashboard')
        return render(request, 'inventory/add.html', {'form': form})

@login_required
def dashboard(request):
    vehicles = Vehicle.objects.all()
    paginator = Paginator(vehicles, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)

    context = {
        'listing': paged_vehicles
    }
    return render(request, 'inventory/dashboard.html', context)
