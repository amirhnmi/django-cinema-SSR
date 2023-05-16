from django.contrib import admin
from .models import SalesTable

# Register your models here.

class SalesTableAdmin(admin.ModelAdmin):
    list_display=["movie_name","director","price","last_update"]


admin.site.register(SalesTable,SalesTableAdmin)