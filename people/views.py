from django.shortcuts import render
from .models import Cafe


def home(request):
    cafes = Cafe.objects.all()
    return render(request, 'index.html', {'cafes': cafes})
