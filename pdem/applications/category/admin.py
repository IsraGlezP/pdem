from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'is_published')
    list_display_links = ('id', 'category')
    list_filter = ('category',)
    list_editable = ('is_published',)
    search_fields = ('category',)

admin.site.register(Category, CategoryAdmin)
