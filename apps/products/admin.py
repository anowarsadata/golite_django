from django.contrib import admin
from .models import Product, ProductVariant, ProductImage

# Inline for variants
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    fields = ['attributes', 'price', 'stock']
    readonly_fields = []
    show_change_link = True  # Allows editing variant in its own page if needed

# Inline for images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'is_main']
    readonly_fields = []
    show_change_link = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    list_filter = ['created_at', 'updated_at']
    inlines = [ProductVariantInline, ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}  # Optional: lets admin see slug while typing

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'attributes', 'price', 'stock']
    search_fields = ['product__name', 'attributes']
    list_filter = ['product']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_main']
    search_fields = ['product__name']
    list_filter = ['is_main']
