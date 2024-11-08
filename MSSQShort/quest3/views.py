from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def quest3(request):
    if request.method == "GET":
        return render(request, 'questionario3.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")
