from django.contrib import admin

# Register your models here.
from src.apps.product.models import Product, ProductImage, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name", 
        "slug",
        'is_main',
    ]
    list_filter = [
        "is_main"
    ]
    search_fields = [
        "name"
    ]
    prepopulated_fields = {"slug": ("name", )}



class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 5




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImageInline]
    list_display = [
        "title",
        "category",
        "price",
        "is_active",
        "created_at",
        "updated_at"
    ]
    list_filter = [
        "category",
        "price",
        "created_at",
        "is_active",
    ]
    search_fields = [
        "title",
        "description"
    ]
    