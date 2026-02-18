from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='q1_index'),
    path('result/', views.result, name='q1_result'),
]
