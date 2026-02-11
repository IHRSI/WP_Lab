from django.urls import path
from . import views

urlpatterns = [
    path('', views.magazine_cover, name='magazine_cover'),
]
