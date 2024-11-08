from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def quest2(request):
    if request.method == "GET":
        return render(request, 'questionario2.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")
