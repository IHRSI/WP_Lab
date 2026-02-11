from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_formatter, name='formatter'),
]
