from django.urls import path
from . import views

urlpatterns = [
    path('initial', views.index, name="initial"),
    path('loginAdm', views.login_Adm, name="loginAdm"),
    path('loginUser', views.login_User, name="loginUser")
]
