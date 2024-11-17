from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import quest2


def questionario2(request):
    if request.method == "GET":
        return render(request, 'questionario2.html')

    elif request.method == "POST":
        altura = request.POST.get('altura')
        cintura = request.POST.get('cintura')
        peso = request.POST.get('peso')
        imc = request.POST.get('imc')
        pressao = request.POST.get('pressao')
        oximetria = request.POST.get('oximetria')
        frequencia_card = request.POST.get('frequencia_card')

        quest2_envio = quest2(altura=altura, cintura=cintura, peso=peso, imc=imc,
                              pressao=pressao, oximetria=oximetria, frequencia_card=frequencia_card)

        quest2_envio.save()

        return HttpResponse("oIE moreh")
