from django.contrib import admin

from .models import Subscription, Payment, StripeCustomer
# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "stripe_subscription_id", "status")
    list_filter = ("status",)
    search_fields = ("user__username", "stripe_subscription_id")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status")
    list_filter = ("status",)
    search_fields = ("user__username",)

@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "stripe_customer_id")
    search_fields = ("user__username", "stripe_customer_id")