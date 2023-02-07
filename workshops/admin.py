from django.contrib import admin
from workshops.models import Workshops

@admin.register(Workshops)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name','date','current','price','workshop_image','description')
    list_filter = ('current',)
    search_fields = ('name',)
