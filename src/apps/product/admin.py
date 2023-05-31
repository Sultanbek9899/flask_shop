from django.contrib import admin

# Register your models here.
from src.apps.product.models import Product, ProductImage, Category

admin.site.register(Category)

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
    