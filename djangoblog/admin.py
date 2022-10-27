from django.contrib import admin, messages
from django.utils.translation import ngettext

# Register your models here.

from .models import Post, Comment


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

@admin.action(description='Delete Selected Post')
def delete_post(modeladmin, request, queryset):
    queryset.update(status='p')
    self.message_user(request, ngettext(
        '%d post was successfully deleted.',
        '%d posts were successfully deleted.',
        updated,
    ) % updated, messages.SUCCESS)


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'created_at']
    list_filter = ['created_at']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}
    actions = [delete_post]
    
@admin.action(description='Delete Selected Comment')
def delete_comment(modeladmin, request, queryset):
    queryset.update(status='p')
    self.message_user(request, ngettext(
        '%d comment was successfully deleted.',
        '%d comments were successfully deleted.',
        updated,
    ) % updated, messages.SUCCESS)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['fname', 'post', 'created_at']
    list_filter = ['created_at']
    actions = [delete_comment]
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
