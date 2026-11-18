from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
    path("", views.checkout, name="checkout"),
]