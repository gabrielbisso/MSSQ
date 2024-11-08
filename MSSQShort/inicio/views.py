from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        return render(request, 'initial.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")
