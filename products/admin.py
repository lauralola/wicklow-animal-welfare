from django.contrib import admin
from .models import Product, Category, Rating


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'featured_image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'public_name',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'product',
        'rating',
    )


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Rating, RatingAdmin)
