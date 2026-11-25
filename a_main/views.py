from django.shortcuts import render


def index(request):
    return render(request, 'a_main/index.html')
