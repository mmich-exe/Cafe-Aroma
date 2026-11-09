from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cafe
from .forms import CafeForm

from .models import Cafe, TipoCafe

def lista_carta(request):
    cafes = Cafe.objects.all()
    tipos = TipoCafe.objects.all() # Para llenar el select de categorías

    visitas = request.session.get('contador_visitas_carta', 0)
    visitas += 1
    request.session['contador_visitas_carta'] = visitas

    # 1. Búsqueda por nombre o código
    query = request.GET.get('q')
    if query:
        cafes = cafes.filter(nombre__icontains=query)

    # 2. Filtro por tipo de café
    tipo_id = request.GET.get('tipo')
    if tipo_id:
        cafes = cafes.filter(tipo_id=tipo_id)

    # 3. Ordenamiento por precio (o nombre)
    orden = request.GET.get('orden')
    if orden == 'precio_asc':
        cafes = cafes.order_by('precio')
    elif orden == 'precio_desc':
        cafes = cafes.order_by('-precio')

    return render(request, 'carta/lista_carta.html', {
        'cafes': cafes,
        'tipos': tipos,
        'query': query or '',
        'tipo_seleccionado': tipo_id or '',
        'orden_seleccionado': orden or ''
    })

def detalle_cafe(request, pk):
    cafe = get_object_or_404(Cafe, pk=pk)
    return render(request, 'carta/detalle_cafe.html', {'cafe': cafe})

# CRUD
def crear_cafe(request):
    if request.method == 'POST':
        form = CafeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carta')
    else:
        form = CafeForm()
    
    return render(request, 'carta/crear_cafe.html', {'form': form})

def editar_cafe(request, pk):
    cafe = get_object_or_404(Cafe, pk=pk)
    if request.method == 'POST':
        form = CafeForm(request.POST, instance=cafe)
        if form.is_valid():
            form.save()
            return redirect('lista_carta')
    else:
        form = CafeForm(instance=cafe)
    
    return render(request, 'carta/editar_cafe.html', {'form': form, 'cafe': cafe})

def eliminar_cafe(request, pk):
    cafe = get_object_or_404(Cafe, pk=pk)
    if request.method == 'POST':
        cafe.delete()
        return redirect('lista_carta')
    return render(request, 'carta/eliminar_cafe.html', {'cafe': cafe})