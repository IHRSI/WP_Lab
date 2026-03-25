from django.urls import path

from . import views

app_name = 'q2'

urlpatterns = [
    path('', views.index, name='index'),
]
