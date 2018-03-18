from django.shortcuts import render
from .models import Cafe
from .forms import RegisterForm


def home(request):
    cafes = Cafe.objects.all()
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html', {'register': form})

    return render(request, 'index.html', {'cafes': cafes, 'form': form})
