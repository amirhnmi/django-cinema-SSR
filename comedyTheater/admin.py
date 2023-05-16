from django.contrib import admin
from .models import ComedyTheater

# Register your models here.

class ComedyTheaterAdmin(admin.ModelAdmin):
    list_display = ["id","title","director", "producer", "production_date", "release_date", "create_date", "publish_date"]


admin.site.register(ComedyTheater,ComedyTheaterAdmin)