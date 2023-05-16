from django.contrib import admin
from .models import ArtAndExpriens

# Register your models here.

class ArtAndExpriensAdmin(admin.ModelAdmin):
    list_display = ["id","title","director", "producer", "production_date", "release_date", "create_date", "publish_date"]


admin.site.register(ArtAndExpriens,ArtAndExpriensAdmin)