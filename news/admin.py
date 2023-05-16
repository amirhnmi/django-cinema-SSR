from django.contrib import admin
from .models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display=["title","description","news_text","author","news_date","publish_date"]

admin.site.register(News,NewsAdmin)