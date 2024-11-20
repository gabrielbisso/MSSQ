from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db import models
from django.db import connection
from quest1.models import banco_quest1
from quest2.models import banco_quest2
from quest3.models import banco_quest3

credencialglobal = None


def login_Adm(request):
    if request.method == "GET":
        return render(request, 'loginAdm.html')

    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if usuario == "Admin" and senha == "12345":
            return render(request, 'resultados.html')

        elif usuario != "Admin" or senha != "12345":
            messages.error(request, "Usuário ou senha incorretos")
            return render(request, 'loginAdm.html')


def login_User(request):
    global credencialglobal

    if request.method == "GET":
        disable_buttonfalse = False
        disable_button = True
        return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_button})

    elif request.method == "POST":
        credencial = request.POST.get('credencial')

        # Verificando a existência dos registros nos três bancos de dados
        q1 = banco_quest1.objects.filter(id=credencial).first()
        q2 = banco_quest2.objects.filter(id=credencial).first()
        q3 = banco_quest3.objects.filter(id=credencial).first()

        # Definindo as variáveis de existência com base na consulta
        q1_exist = q1 is not None
        q2_exist = q2 is not None
        q3_exist = q3 is not None

        # Se a credencial estiver vazia, desabilita todos os botões
        if credencial == "":
            disable_button = True
            return render(request, 'loginUser.html', {
                'disable_button1': disable_button,
                'disable_button2': disable_button,
                'disable_button3': disable_button,
                'credencial': credencial
            })

        # Se q1 não existe, desabilita o botão correspondente
        elif not q1_exist:
            credencialglobal = credencial
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {
                'disable_button1': disable_buttonfalse,
                'disable_button2': disable_button,
                'disable_button3': disable_button,
                'credencial': credencial
            })

        # Se q1 existe mas q2 não, desabilita o botão de q2
        elif q1_exist and not q2_exist:
            credencialglobal = credencial
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {
                'disable_button1': disable_button,
                'disable_button2': disable_buttonfalse,
                'disable_button3': disable_button,
                'credencial': credencial
            })

        # Se q2 existe mas q3 não, desabilita o botão de q3
        elif q2_exist and not q3_exist:
            credencialglobal = credencial
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {
                'disable_button1': disable_button,
                'disable_button2': disable_button,
                'disable_button3': disable_buttonfalse,
                'credencial': credencial
            })

        # Se todos os questionários existem, exibe uma mensagem
        elif q3_exist:
            credencialglobal = credencial
            return HttpResponse("Você já preencheu todos os questionários")


def quest1(request):
    return render(request, 'questionario1.html', {'credencial': credencialglobal})


def quest2(request):
    return render(request, 'questionario2.html', {'credencial': credencialglobal})


def quest3(request):
    return render(request, 'questionario3.html', {'credencial': credencialglobal})


def resultados(request):
    return render(request, 'resultados.html')
