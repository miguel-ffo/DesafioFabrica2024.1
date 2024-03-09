from django.contrib import admin
from django.urls import path
from filme.serializers import FilmeSerializer

from . import views

urlpatterns = [
    path('', views.RegisterFilmeView.as_view()),
]