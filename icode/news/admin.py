from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',
                    'created_at', 'updated_at',
                    'preview_image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


admin.site.register(News, NewsAdmin)

