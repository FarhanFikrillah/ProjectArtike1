from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import *
from mysite.authentication import login, logout, registrasi
#
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name="welcome"),
    
    path('artikel/<int:id>', detail_artikel, name="detail_artikel"),
    path('artikel-not-found', not_found_artikel, name="not_found_artikel"),
    path('buku', buku,name="buku"),
    path('kontak', kontak,name="kontak"),
    
    path('dashboard', dashboard, name="dashboard"),
    path('dashboard/artikel_list', artikel_list, name="artikel_list"),
    
    path('dashboard/', include("artikel.urls")),

    
    ######################### Authentication ##########################
    path('auth-login', login, name="login"),
    path('auth-logout', logout, name="logout"),
    path('auth-registrasi', registrasi, name="registrasi"),


]

################################## Bagian media ############################

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

################################ CKeditor5 ###################################

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#########################################################################
