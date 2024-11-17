from django.urls import path
from . import views

urlpatterns = [
    path('questionario3', views.questionario3, name="questionario3")
]
