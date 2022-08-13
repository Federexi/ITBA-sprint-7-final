
from django.urls import path
from . import views

urlpatterns = [
    path('prestamos/', views.index2, name = 'prestamos'),

]