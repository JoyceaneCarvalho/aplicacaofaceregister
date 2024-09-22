from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfilaluno(request):
    return render(request, 'faceregister/perfilaluno.html')

def consfrequencia(request):
    return render(request, 'faceregister/consfrequencia.html')

def perfilprof(request):
    return render(request, 'faceregister/perfilprof.html')

def loginprof(request):
    return render(request, 'faceregister/loginprof.html')

def loginaluno(request):
    return render(request, 'faceregister/loginaluno.html')

def cadastroaluno(request):
    return render(request, 'faceregister/cadastroaluno.html')

def cadastroprof(request):
    return render(request, 'faceregister/cadastroprof.html')

def realizarfreq(request):
    return render(request, 'faceregister/realizarfreq.html')

def consfrequencia_prof(request):
    return render(request, 'faceregister/consfrequencia_prof.html')

def cadaluno(request):
    return render(request, 'faceregister/cadaluno.html')


