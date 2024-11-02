from django.shortcuts import render
from django.http import HttpResponse


def login_Adm(request):
    if request.method == "GET":
        return render(request, 'loginAdm.html')

    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        if usuario == "Admin" and senha == "12345":
            return HttpResponse("Você foi logado com sucesso")

        elif usuario != "Admin" or senha != "12345":
            return HttpResponse("Você não tem cadastro moreh")
