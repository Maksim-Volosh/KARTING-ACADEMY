from django.contrib import admin
from app_news.models import News
    
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    
    
    


admin.site.register(News, NewsAdmin)