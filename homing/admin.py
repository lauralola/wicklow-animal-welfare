from django.contrib import admin
from .models import Dog, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Dog)
class DogAdmin(SummernoteModelAdmin):

    list_display = ('dog_name', 'slug', 'status', 'created_on')
    search_fields = ['dog_name', 'content',]
    list_filter = ('status', 'created_on', 'size', 'sex')
    prepopulated_fields = {'slug': ('dog_name',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'body', 'dog', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
