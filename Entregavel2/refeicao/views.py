from django.shortcuts import render

def home(request):
    return render(request, 'refeicao/index.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'refeicao/login.html', {'erro': 'Login inválido'})

    return render(request, 'refeicao/login.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        return redirect('login')

    return render(request, 'refeicao/cadastro.html')

def plsemanal(request):
    return render(request, 'refeicao/plsemanal.html')

def cadrefeicao(request):
    return render(request, 'refeicao/cadrefeicao.html')

def compras(request):
    return render(request, 'refeicao/compras.html')

def perfil(request):
    return render(request, 'refeicao/perfil.html')

def almoco(request):
    return render(request, 'refeicao/almoco.html')

def cafemanha(request):
    return render(request, 'refeicao/cafemanha.html')

def lanche(request):
    return render(request, 'refeicao/lanche.html')

def jantar(request):
    return render(request, 'refeicao/jantar.html')