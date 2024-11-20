from django.urls import path
from . import views

urlpatterns = [
    path('resultados', views.resultados, name="resultados")
]
