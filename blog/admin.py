from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin

from .models import Category, Post


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('slug', 'name', 'cnt')
    prepopulated_fields = {"slug": ("name",)}

    def cnt(self, obj):
        return len(obj.post_set.all())

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'title', 'admin_categories', 'status')
    list_filter = ('status', )
    def admin_categories(self, obj):
        return ", ".join([a.name for a in obj.categories.all()])



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)