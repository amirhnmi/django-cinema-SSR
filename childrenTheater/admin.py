from django.contrib import admin
from .models import ChildreTheater

# Register your models here.


class ChildreTheaterAdmin(admin.ModelAdmin):
    list_display = ["id","title","director", "producer", "production_date", "release_date", "create_date", "publish_date"]


admin.site.register(ChildreTheater,ChildreTheaterAdmin)