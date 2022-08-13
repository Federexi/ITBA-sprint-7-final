
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def act (request):
    return render (request, 'Cuentas/template/Cuentas/actividad.html')

@login_required
def conf (request):
    return render (request, 'Cuentas/template/Cuentas/configuracion.html')

@login_required
def cuenta (request):
    return render (request, 'Cuentas/template/Cuentas/cuenta.html')

@login_required
def hub (request):
    return render (request, 'Cuentas/template/Cuentas/hub.html')

@login_required
def inv (request):
    return render (request, 'Cuentas/template/Cuentas/inversiones.html')
    
@login_required
def seg (request):
    return render (request, 'Cuentas/template/Cuentas/seguridad.html')

@login_required
def transf (request):
    return render (request, 'Cuentas/template/Cuentas/transferencias.html')