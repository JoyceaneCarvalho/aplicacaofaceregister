from django.contrib import admin
from django.urls import path
from .views import index, second, telaaluno

urlpatterns = [
    path('', index, name='index'),
    path('second/', second, name='second'),
    path('telaaluno/', telaaluno, name='telaaluno'),

]