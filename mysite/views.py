from django.shortcuts import render, redirect
from artikel.models import Kategori, Artikel

def welcome(request):
    template_name = "landingpage/index.html"
    kategori = Kategori.objects.all()
    artikel = Artikel.objects.all()

    for k in kategori:
        print(k)
    for a in artikel:
        print(a)

    context = {
        "title":"selamat datang",
        "kategori":kategori,
        "artikel":artikel
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = "landingpage/detail.html"
    try:
        artikel = Artikel.objects.get(id=id)
    except Artikel.DoesNotExist :
        return redirect(not_found_artikel)

    artikel_lainnya = Artikel.objects.all().exclude(id=id)

    context = {
        "title":"selamat datang",
        "artikel": artikel,
        "artikel_lainnya":artikel_lainnya,
    }
    return render(request, template_name, context)

def not_found_artikel(request):
    template_name = "not-found-artikel.html"
    return render(request, template_name)

def buku(request):
    template_name = "buku.html"
    context = {
        "title":"halaman buku"
    }
    return render(request, template_name, context)


def kontak(request):
    template_name="kontak.html"
    context={
        "title": "kontak",
    }
    return render(request, template_name,context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    template_name="dashboard/index.html"
    context={
        "title": "selamat datang ",
    }
    return render(request, template_name,context)

def artikel_list(request):
    template_name="dashboard/artikel_list.html "
    context={
        "title": "selamat datang ",
    }
    return render(request, template_name,context)