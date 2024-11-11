from django.urls import path
from . import views

urlpatterns = [
    path('questionario3', views.quest3, name="quest3")
]
