from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def telaaluno(request):
    return render(request, 'telaaluno.html')
