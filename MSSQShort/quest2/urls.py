from django.urls import path
from . import views

urlpatterns = [
    path('questionario2', views.questionario2, name="questionario2")
]
