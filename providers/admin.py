from django.contrib import admin
from providers.models import Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email','condition')
    list_filter = ('condition',)
    search_fields = ('name','phone_number')

