from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def quest1(request):
    if request.method == "GET":
        return render(request, 'questionario1.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")
