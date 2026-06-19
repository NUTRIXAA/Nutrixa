from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('plsemanal/', views.plsemanal, name='plsemanal'),
    path('dtrefeicao/', views.dtrefeicao, name='dtrefeicao'),
    path('cadrefeicao/', views.cadrefeicao, name='cadrefeicao'),
    path('compras/', views.compras, name='compras'),
    path('perfil/', views.perfil, name='perfil'),
]