from django.shortcuts import render
from .models import Refeicao
from django.shortcuts import get_object_or_404

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

def favoritos(request):
    refeicoes = Refeicao.objects.filter(favorita=True)

    return render(
        request,
        'refeicao/favoritos.html',
        {'refeicoes': refeicoes}
    )

from django.shortcuts import redirect

def favoritar_refeicao(request, id):
    refeicao = get_object_or_404(Refeicao, id=id)

    refeicao.favorita = True
    refeicao.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def desfavoritar_refeicao(request, id):
    refeicao = get_object_or_404(Refeicao, id=id)

    refeicao.favorita = False
    refeicao.save()

    return redirect('favoritos')