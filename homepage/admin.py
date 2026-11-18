from django.contrib import admin

from .models import Profile, Transaction

# Register your models here.
admin.site.site_header = "Secure Money Vault Admin"
admin.site.site_title = "Secure Money Vault Admin Portal"


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "user", "amount", "type", "category", "date")
    list_filter = ("type", "category", "date")
    search_fields = ("transaction_id", "description", "user__username")
    ordering = ("-date",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "currency")
    list_filter = ("currency",)
    search_fields = ("user__username",)
