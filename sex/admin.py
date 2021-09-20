from django.contrib import admin
from . models import Category, Blogger, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Blogger)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'active')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
