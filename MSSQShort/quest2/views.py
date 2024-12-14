from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import banco_quest2


def questionario2(request):
    if request.method == "GET":
        return render(request, 'questionario2.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        altura = request.POST.get('altura')
        cintura = request.POST.get('cintura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        pressao = request.POST.get('pressao')
        oximetria = request.POST.get('oximetria')
        frequencia_card = request.POST.get('frequencia_card')

        if id is not None:
            quest2_envio = banco_quest2(id=id, altura=altura, cintura=cintura, peso=peso, imc=imc,
                                        pressao=pressao, oximetria=oximetria, frequencia_card=frequencia_card)

            quest2_envio.save()

        return render(request, 'questionario3.html', {"id": id})
