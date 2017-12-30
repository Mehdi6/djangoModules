from django.contrib import admin
from .models import Category, Product, ProductMedia, Brand

# Register your models here.
@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_cat', 'slug']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture' ]
  
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'instock', 'price', 'brand', 'category']

@admin.register(ProductMedia)
class PoductMediaModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'product', 'isPrimary']