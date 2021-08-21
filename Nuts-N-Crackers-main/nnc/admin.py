from django.contrib import admin
from .models import Category, CategoryProduct, Order, OrderProduct,Product


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Order)
admin.site.register(OrderProduct)
