from django.contrib import admin
from django.contrib.admin import register

from .models import Transaction


@register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'payment_status']
    search_fields = ['user']
