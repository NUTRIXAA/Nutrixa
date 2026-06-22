from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), 


    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('plsemanal/', views.plsemanal, name='plsemanal'),
    path('cadrefeicao/', views.cadrefeicao, name='cadrefeicao'),
    path('compras/', views.compras, name='compras'),
    path('perfil/', views.perfil, name='perfil'),
    path('almoco/', views.almoco, name='almoco'),
    path('cafemanha/', views.cafemanha, name='cafemanha'),
    path('lanche/', views.lanche, name='lanche'),
    path('jantar/', views.jantar, name='jantar'),
]