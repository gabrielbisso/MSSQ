from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import banco_quest1


def questionario1(request):
    if request.method == "GET":
        return render(request, 'questionario1.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        idade = request.POST.get('idade')
        sexo = request.POST.get('sexo')
        carros = request.POST.get('pergunta1')
        autocarros = request.POST.get('pergunta2')
        comboios = request.POST.get('pergunta3')
        avioes = request.POST.get('pergunta4')
        embarcacao_pequena = request.POST.get('pergunta5')
        navios = request.POST.get('pergunta6')
        baloicos = request.POST.get('pergunta7')
        carroseis = request.POST.get('pergunta8')
        montanha_russa = request.POST.get('pergunta9')
        carros2 = request.POST.get('pergunta1.2')
        autocarros2 = request.POST.get('pergunta2.2')
        comboios2 = request.POST.get('pergunta3.2')
        avioes2 = request.POST.get('pergunta4.2')
        embarcacao_pequena2 = request.POST.get('pergunta5.2')
        navios2 = request.POST.get('pergunta6.2')
        baloicos2 = request.POST.get('pergunta7.2')
        carroseis2 = request.POST.get('pergunta8.2')
        montanha_russa2 = request.POST.get('pergunta9.2')

        if id is not None:
            quest1_envio = banco_quest1(id=id, idade=idade, sexo=sexo, carros=carros, autocarros=autocarros,
                                        comboios=comboios, avioes=avioes, embarcacao_pequena=embarcacao_pequena, navios=navios, baloicos=baloicos, carroseis=carroseis, montanha_russa=montanha_russa, carros2=carros2, autocarros2=autocarros2, comboios2=comboios2, avioes2=avioes2, embarcacao_pequena2=embarcacao_pequena2, navios2=navios2, baloicos2=baloicos2, carroseis2=carroseis2, montanha_russa2=montanha_russa2)
            quest1_envio.save()

        return render(request, 'questionario2.html', {"id": id})
