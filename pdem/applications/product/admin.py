from django.contrib import admin

from .models import Product, Variant

class VariantInline(admin.TabularInline):
    model = Variant


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_top')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    list_editable = ('is_top',)
    search_fields = ('name',)
    list_per_page = 25

    model = Variant
    inlines = [
        VariantInline,
    ]


class VariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'value')
    list_display_links = ('id', 'product')
    list_filter = ('product',)
    search_fields = ('product',)
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
