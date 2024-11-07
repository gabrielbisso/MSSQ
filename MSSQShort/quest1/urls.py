from django.urls import path
from . import views

urlpatterns = [
    path('questionario1', views.quest1, name="qeust1")
]
