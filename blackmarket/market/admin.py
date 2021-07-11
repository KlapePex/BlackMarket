from django.contrib import admin
from .models import Profile, Product, Order, OrderItem, ShippingAddress


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('complete',)


class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ('order',)


admin.site.register(Profile)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress)

