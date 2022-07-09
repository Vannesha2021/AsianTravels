from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'updated_on')
    list_display = ('title', 'slug', 'status', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'blog', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'content']
    actions = ['approve_comments']

    def approve_comments(self,request, queryset):
        queryset.update(approved=True)