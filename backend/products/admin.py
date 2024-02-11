from django.contrib import admin
from .models import Category, Product, Brand, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")
    search_fields = ("name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "quantity", "price", "is_published", "aviable")
    list_filter = ("name", "price")
    prepopulated_fields = {"url": ("name",)}
    save_on_top = True
    save_as = True
    
    
