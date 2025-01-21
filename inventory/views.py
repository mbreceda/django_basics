from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.paginator import Paginator
from django.contrib.auth.models import User

from .models import Vehicle


def inventory(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        make = request.POST['make']
        model = request.POST['model']
        description = request.POST['description']
        color = request.POST['color']
        doors = request.POST['doors']
        lot_number = request.POST['lot_number']

        if request.user.is_authenticated:
            vehicle = Vehicle(user_id=user_id, make=make, model=model, description=description, color=color, doors=doors, lot_number=lot_number)
            vehicle.save()
            messages.success(request, 'Vehicle added')
            return redirect('inventory')
        
    return render(request, 'inventory/inventory.html')

def dashboard(request):
    vehicles = Vehicle.objects.order_by('-created_at').filter(user_id=request.user.id)

    paginator = Paginator(vehicles, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)

    context = {
        'vehicles': paged_vehicles
    }
    return render(request, 'inventory/dashboard.html', context)

        
