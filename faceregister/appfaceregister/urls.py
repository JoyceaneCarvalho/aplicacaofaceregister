from django.urls import path

from .views import index, perfilaluno, perfilprof, loginprof, loginaluno, cadastroaluno, cadastroprof, consfrequencia, realizarfreq, consfrequencia_prof, cadaluno

urlpatterns = [
    path('', index, name='index'),
    path('perfilaluno/', perfilaluno, name='perfilaluno'),
    path('perfilprof/', perfilprof, name='perfilprof'),
    path('loginprof/', loginprof, name='loginprof'),
    path('loginaluno/', loginaluno, name='loginaluno'),
    path('cadastroaluno/', cadastroaluno, name='cadastroaluno'),
    path('cadastroprof/', cadastroprof, name='cadastroprof'),
    path('consfrequencia/', consfrequencia, name='consfrequencia'),
    path('realizarfreq/', realizarfreq, name='realizarfreq'),
    path('consfrequencia_prof/', consfrequencia_prof, name='consfrequencia_prof'),
    path('cadaluno/', cadaluno, name='cadaluno'),
]