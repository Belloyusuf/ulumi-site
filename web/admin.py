from django.contrib import admin
from .models import News, Comment



admin.site.site_header = "Madarasatul Ulumi Wal-Qur'an Takur Site"
admin.site.site_title = "mr nice"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ('title','author')
    list_display = ('title', 'body','author')
    prepopulated_fields = {'slug':['title']}
    raw_id_fields = ('author',)
    date_hierarchy = ('created')
    ordering = ('created',)
   



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'email', 'news', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
