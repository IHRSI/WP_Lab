from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='a1_index'),
    path('add/', views.add_items, name='a1_add'),
]
