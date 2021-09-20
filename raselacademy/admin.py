from django.contrib import admin
from . models import Category, Blog, Comment

# Register your models here.

class CategoryInline(admin.StackedInline):
    model = Category.blog.through
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("blog",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

