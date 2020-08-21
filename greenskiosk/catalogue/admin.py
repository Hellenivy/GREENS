from django.contrib import admin
from .models import Product,ProductSupplier,ProductCategory,ProductImage
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductSupplier)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)