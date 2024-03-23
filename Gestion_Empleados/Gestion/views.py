from django.shortcuts import render
from django.http import HttpResponse
from .models import Salarios, PuestoTrabajo

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def salario(request):
    return render(request, 'salary.html', {})

def save_salario(request):
    monto = request.GET['monto']
    if 'cobro_ano' in request.GET:
        cobro_ano = True
    else:
        cobro_ano = False
    if 'pago_extra' in request.GET:
        pago_extra = True
    else:
        pago_extra = False
    
    new_salario = Salarios.objects.create(monto = monto, cobro_ano=cobro_ano, pago_extra=pago_extra)

    print(monto)
    return HttpResponse('Se registro esta monda')

def trabajo(request):
    #listar los salarios
    salaritos = Salarios.objects.all()
    return render(request, 'job.html', {
    'salaritos': salaritos})

def save_trabajo(request):
    nombre_cargo = request.GET['name']
    descripcion = request.GET['descripcion']
    salarito_id = request.GET['salarito_id']
    salario = Salarios.objects.get(id=salarito_id)
    new_trabajo = PuestoTrabajo.objects.create(nombre_cargo=nombre_cargo, descripcion=descripcion, salario_monto=salario)
    return HttpResponse('Se registro esta monda 2.0')