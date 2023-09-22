from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        username = request.POST.get('username')
        celular = request.POST.get('celular')
        telefone_fixo = request.POST.get('telefone_fixo')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not(senha == confirmar_senha):
            messages.add_message(request, constants.INFO, 'As senhas não conferem!')
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.add_message(request, constants.INFO, 'O usuário já existe!')
            return redirect(reverse('cadastro'))
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect(reverse('login'))
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = username.POST.get('username')
        senha = senha.POST.get('senha')
        
        user = auth.authenticate(username=username, password=senha)
        
        if not user:
            messages.add_message(request, constants.SUCCESS, 'Usuário não ecziste!')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento/')