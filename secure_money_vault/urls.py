"""
URL configuration for secure_money_vault project.

"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from allauth.account.decorators import secure_admin_login

admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)  # type: ignore

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('checkout/', include('checkout.urls')),
    path('', include('homepage.urls')),
    
]
