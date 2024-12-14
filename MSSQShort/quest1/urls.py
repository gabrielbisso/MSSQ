from django.urls import path
from . import views

urlpatterns = [
    path('questionario1', views.questionario1, name="questionario1")
]
