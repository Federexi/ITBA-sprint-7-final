
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView , logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homebanking/', include('Clientes.urls')),
    path('homebanking/', include('Cuentas.urls')),
    path('homebanking/', include('Login.urls')),
    path('homebanking/', include('Prestamos.urls')),
    path('homebanking/', include('Tarjetas.urls')),
    path('logout/', logout_then_login, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
