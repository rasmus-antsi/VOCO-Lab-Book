from django.urls import path

from . import views

app_name = 'a_main'

urlpatterns = [
    path('', views.index, name='index'),
]
