
from django.urls import path
from . import views

urlpatterns = [
    path('actividad/',views.act, name = 'act'),
    path('configuracion/', views.conf, name = 'conf'),
    path('cuenta/', views.cuenta, name = 'cuenta'),
    path('hub/',  views.hub, name = 'hub'),
    path('inversiones/', views.inv, name = 'inv'),
    path('seguridad/', views.seg, name = 'seg'),
    path('transferencias/', views.transf, name = 'transf'),
]