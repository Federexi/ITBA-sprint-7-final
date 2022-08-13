from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index2 (request):
    return render (request, 'Prestamos/template/Prestamos/prestamos.html')
