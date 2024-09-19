from django.urls import path

from .views import index, perfilaluno, perfilprof, loginprof, loginaluno, cadastroaluno, cadastroprof

urlpatterns = [
    path('', index, name='index'),
    path('perfilaluno/', perfilaluno, name='perfilaluno'),
    path('perfilprof/', perfilprof, name='perfilprof'),
    path('loginprof/', loginprof, name='loginprof'),
    path('loginaluno/', loginaluno, name='loginaluno'),
    path('cadastroaluno/', cadastroaluno, name='cadastroaluno'),
    path('cadastroprof/', cadastroprof, name='cadastroprof'),
]