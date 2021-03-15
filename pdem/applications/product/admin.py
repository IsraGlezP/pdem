from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_top')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_top',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)
