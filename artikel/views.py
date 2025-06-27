from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group


from artikel.models import Kategori, Artikel
from artikel.forms import KategoriForms, ArtikelForms
# Create your views here.
# def artikel_list(request):
#     template_name = "artikel_list.html"
#     kategori = Kategori.objects.all()
#     artikel = Artikel.objects.all()
#     context = {
#         "kategori":kategori,
#         "artikel":artikel,
#     }
#     return render(request, template_name, context)
def in_operator(user):
    get_user = user.groups.filter(name='Operator').count()
    if get_user == 0:
        return False
    else:
        return True
##################### USER BIASA ######################
@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = Artikel.objects.filter(created_by=request.user)
    context = {
        "artikel":artikel,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/admin/artikel_form.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Membuat Artikel')

        return redirect(artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_form.html"
    artikel = Artikel.objects.get(id=id_artikel, created_by=request.user)
    
    if request.method == "POST":
        forms = ArtikelForms(request.POST,request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan Update Artikel')
        return redirect(artikel_list)
    
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
            try:
                Artikel.objects.get(id=id_artikel,created_by=request.user).delete()
                messages.success(request, 'Berhasil menghapus Artikel')
            except:
                messages.error(request, 'Gagal menghapus Kategori')
            return redirect(artikel_list)
###################### ADMIN #########################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    context = {
        "kategori":kategori
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_form.html"
    if request.method == "POST":
        forms = KategoriForms(request.POST)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Menambahkan Kategori')

        # nama_kategori = request.POST.get('nama_kategori')
        # if nama_kategori:
        #     Kategori.objects.create(
        #         nama = nama_kategori,
        #         created_by = request.user,
        #     )
        return redirect(admin_kategori_list)
    forms = KategoriForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_form.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        forms = KategoriForms(request.POST, instance=kategori)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan Update Kategori')
        return redirect(admin_kategori_list)
    forms = KategoriForms(instance=kategori)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_kategori_delete(request, id_kategori):
            try:
                Kategori.objects.get(id=id_kategori).delete()
                messages.success(request, 'Berhasil menghapus Kategori')
            except:
                messages.error(request, 'Gagal menghapus Kategori')

            return redirect(admin_kategori_list)
################# artikel ###################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = Artikel.objects.all()
    context = {
        "artikel":artikel
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_form.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil Membuat Artikel')

        return redirect(admin_artikel_list)
    forms = ArtikelForms()
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_form.html"
    artikel = Artikel.objects.get(id=id_artikel)
    
    if request.method == "POST":
        forms = ArtikelForms(request.POST,request.FILES, instance=artikel)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
            messages.success(request, 'Berhasil melakukan Update Artikel')
        return redirect(admin_artikel_list)
    
    forms = ArtikelForms(instance=artikel)
    context = {
        "forms":forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_artikel_delete(request, id_artikel):
            try:
                Artikel.objects.get(id=id_artikel).delete()
                messages.success(request, 'Berhasil menghapus Artikel')
            except:
                messages.error(request, 'Gagal menghapus Kategori')
            return redirect(admin_artikel_list)

################################ Management user Oleh Operator #########################################
@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user,
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
@user_passes_test(in_operator, login_url='/')
def admin_management_user_edit(request, user_id):
    template_name = "dashboard/admin/user_edit.html"
    user = get_object_or_404(User, pk=user_id)  # Ambil objek user berdasarkan ID, atau 404 jika tidak ditemukan

    all_groups = Group.objects.all()
    group_user = []
    for group in user.groups.all():
        group_user.append(group.name)

    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff_input = request.POST.get("is_staff")  # Renamed to avoid conflict with user.is_staff
        groups_checked = request.POST.getlist('groups')

        if is_staff_input is None:
            is_staff = False
        else:
            is_staff = True

        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = is_staff
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f"Berhasil update user {user.username}")
        return redirect('admin_management_user_list')  # Redirect ke halaman daftar user setelah berhasil

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user,
        
    }
    return render(request, template_name, context)