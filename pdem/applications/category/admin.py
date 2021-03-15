from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Category, CategoryAdmin)
