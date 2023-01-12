from django.contrib import admin
from supplies.models import Supplies


@admin.register(Supplies)
class SupplieAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock',)
    search_fields = ('name',)
