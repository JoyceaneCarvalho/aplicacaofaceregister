from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfilaluno(request):
    return render(request, 'faceregister/cadastroaluno/perfilaluno.html')

def perfilprof(request):
    return render(request, 'faceregister/cadastroaluno/perfilprof.html')

def loginprof(request):
    return render(request, 'faceregister/loginprof.html')

def loginaluno(request):
    return render(request, 'faceregister/loginaluno.html')

def cadastroaluno(request):
    return render(request, 'faceregister/cadastroaluno.html')

def cadastroprof(request):
    return render(request, 'faceregister/cadastroprof.html')





