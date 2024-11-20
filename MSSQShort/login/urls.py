from django.urls import path
from . import views

urlpatterns = [
    path('loginAdm', views.login_Adm, name="loginAdm"),
    path('loginUser', views.login_User, name="loginUser"),
    path('questionario1', views.quest1, name="questionario1"),
    path('questionario2', views.quest2, name="questionario2"),
    path('questionario3', views.quest3, name="questionario3"),
    path('resultados', views.resultados, name="resultados"),
]
