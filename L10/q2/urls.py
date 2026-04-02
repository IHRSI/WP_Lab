from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="q2_index"),
    path("add/", views.add_product, name="q2_add_product"),
]
