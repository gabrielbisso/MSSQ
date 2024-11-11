from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    if request.method == 'GET':
        return render(request, 'initial.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")


def login_Adm(request):
    if request.method == "GET":
        return render(request, 'loginAdm.html')

    elif request.method == "POST":
        return HttpResponse("oIE moreh")


def login_User(request):
    if request.method == "GET":
        disable_button = True
        return render(request, 'loginUser.html', {'disable_button1': disable_button, 'disable_button2': disable_button, 'disable_button3': disable_button})

    elif request.method == "POST":
        return HttpResponse("oIE moreh")
