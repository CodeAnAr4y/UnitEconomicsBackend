from django.contrib import admin

from django.contrib import admin
from .models import Product, Seller


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'marketplace', 'manager', 'created_at')
    list_filter = ('marketplace', 'created_at', 'manager')
    search_fields = ('marketplace',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager')
    list_filter = ('manager',)
    search_fields = ('name',)