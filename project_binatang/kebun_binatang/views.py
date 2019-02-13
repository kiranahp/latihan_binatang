from django.shortcuts import render, redirect
from .models import hewan
from .form import hewanform


# Create your views here.
def daftar_binatang(request):
    return render(request, 'binatang/daftar_binatang.html', {})

def db_binatang(request):
    binatang = hewan.objects.all()
    return render(request, "binatang/db_binatang.html", {"binatangs":binatang})

def base_binatang(request):
    binatang = hewan.objects.all()
    return render(request, "binatang/base_binatang.html", {"binatangs":binatang})

def input_hewan(request):
    if request.method == "POST":
        form = hewanform(request.POST)
        if form.is_valid:
            form.save()
            return redirect('db_binatang')
    else:
        form = hewanform()
    return render(request, "binatang/hewanform.html", {"form": form})