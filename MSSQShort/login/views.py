from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db import models
from django.db import connection
from quest1.models import banco_quest1
from quest2.models import banco_quest2
from quest3.models import banco_quest3


def login_Adm(request):
    if request.method == "GET":
        return render(request, 'loginAdm.html')

    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if usuario == "Admin" and senha == "12345":
            return HttpResponse("Você foi logado com sucesso")

        elif usuario != "Admin" or senha != "12345":
            messages.error(request, "Usuário ou senha incorretos")
            return render(request, 'loginAdm.html')


def login_User(request):
    if request.method == "GET":
        disable_buttonfalse = False
        disable_button = True
        return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_button})

    elif request.method == "POST":
        credencial = request.POST.get('credencial')
        q1_exist = banco_quest1.objects.get(id=credencial).exists()
        q2_exist = banco_quest2.objects.get(id=credencial).exists()
        q3_exist = banco_quest3.objects.get(id=credencial).exists()

        try:
            q1 = banco_quest1.objects.get(id=credencial)
            q1_exist = True
            q2 = banco_quest2.objects.get(id=credencial)
            q2_exist = True
            q3 = banco_quest3.objects.get(id=credencial)
            q3_exist = True
        except User.DoesNotExist:
            q1_exist = False
            q2_exist = False
            q3_exist = False

        if credencial == "":  # q1.id == None:
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_button, 'credencial': credencial})

        elif q1_exist == False:  # q1.id == None:
            buscar_usuarios()
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_buttonfalse, 'disable_button2': disable_button, 'disable_button3': disable_button, 'credencial': credencial})

        elif q1_exist == True and q2_exist == False:  # q1.id != None:
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_buttonfalse, 'disable_button3': disable_button, 'credencial': credencial})

        if q2_exist == True and q3_exist == False:
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_buttonfalse, 'credencial': credencial})

        elif q3_exist == True:
            return HttpResponse("Você já preencheu todos os questionários")


def quest1(request):
    return render(request, 'questionario1.html')


def quest2(request):
    return render(request, 'questionario2.html')


def quest3(request):
    return render(request, 'questionario3.html')
