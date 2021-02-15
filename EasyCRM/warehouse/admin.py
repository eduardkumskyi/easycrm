from django.contrib import admin
from .models import PrimaryProductSupplier, PrimaryProductType,  PrimaryProduct,\
    ProductSize, ProductType, Product


@admin.register(PrimaryProductSupplier)
class PrimaryProductSupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'link']
    readonly_fields = ['user']
    verbose_name = "Поставщик сырья"
    verbose_name_plural = "Поставщики сырья"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(PrimaryProductType)
class PrimaryProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['user']
    verbose_name = "Тип сырья"
    verbose_name_plural = "Типы сырья"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(PrimaryProduct)
class PrimaryProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'in_stock', 'unit', 'price', 'supplier', 'date_of_receiving']
    list_filter = ['type', 'supplier']
    readonly_fields = ['user']
    verbose_name = "Сырье"
    verbose_name_plural = "Сырье"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['user']
    verbose_name = "Тип продукта"
    verbose_name_plural = "Типы продукта"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['user']
    verbose_name = "Размер"
    verbose_name_plural = "Размеры"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'size', 'in_stock', 'unit', 'standard_price', 'sale_price', 'wholesale_price']
    list_filter = ['type']
    readonly_fields = ['user']
    verbose_name = "Товар"
    verbose_name_plural = "Товары"

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
