from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import banco_quest3


def questionario3(request):
    if request.method == "GET":
        return render(request, 'questionario3.html')

    elif request.method == "POST":
        id = request.POST.get('id')
        nausea = request.POST.get('nausea')
        vomito = request.POST.get('vomito')
        tontura = request.POST.get('tontura')
        suor = request.POST.get('suor')
        palidez = request.POST.get('palidez')
        dorcab = request.POST.get('dorcab')
        cansaco = request.POST.get('cansaco')
        bocejo = request.POST.get('bocejo')
        hiperv = request.POST.get('hiperv')
        outros = request.POST.get('outros')

        if id is not None:
            quest3_envio = banco_quest3(id=id, nausea=nausea, vomito=vomito, tontura=tontura, suor=suor,
                                        palidez=palidez, dorcab=dorcab, cansaco=cansaco, bocejo=bocejo, hiperv=hiperv, outros=outros)

            quest3_envio.save()

        return render(request, 'initial.html')
