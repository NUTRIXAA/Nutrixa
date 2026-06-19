from django.shortcuts import render

def home(request):
    return render(request, 'refeicao/index.html')

def login(request):
    return render(request, 'refeicao/login.html')

def cadastro(request):
    return render(request, 'refeicao/cadastro.html')

def plsemanal(request):
    return render(request, 'refeicao/plsemanal.html')

def dtrefeicao(request):
    return render(request, 'refeicao/dtrefeicao.html')

def cadrefeicao(request):
    return render(request, 'refeicao/cadrefeicao.html')

def compras(request):
    return render(request, 'refeicao/compras.html')

def perfil(request):
    return render(request, 'refeicao/perfil.html')