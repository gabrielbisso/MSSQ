from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


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

        if credencial == "":
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_button, 'credencial': credencial})

        elif credencial == "0":
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_buttonfalse, 'disable_button2': disable_button, 'disable_button3': disable_button, 'credencial': credencial})

        elif credencial == "1":
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_buttonfalse, 'disable_button3': disable_button, 'credencial': credencial})

        elif credencial == "2":
            disable_buttonfalse = False
            disable_button = True
            return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_buttonfalse, 'credencial': credencial})

        elif credencial == "3":
            return HttpResponse("Você já preencheu todos os questionários")


def quest1(request):
    return render(request, 'questionario1.html')


def quest2(request):
    return render(request, 'questionario2.html')


def quest3(request):
    return render(request, 'questionario3.html')
