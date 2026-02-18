from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='q2_first_page'),
    path('second/', views.second_page, name='q2_second_page'),
    path('reset/', views.reset_session, name='q2_reset'),
]
