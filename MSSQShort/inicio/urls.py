from django.urls import path
from . import views

urlpatterns = [
    path('initial', views.index, name="initial"),
]
