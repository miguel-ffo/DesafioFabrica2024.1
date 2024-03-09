from django.contrib import admin
from django.urls import path
from filme.serializers import FilmeSerializer

from . import views

app_name = 'filme'

urlpatterns = [
    path('', views.FilmeListView.as_view()),
]