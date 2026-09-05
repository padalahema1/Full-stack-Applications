from django.contrib import admin

from .models import Restaurant, MenuItem, Order


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "location",
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "restaurant",
        "price",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "item",
        "quantity",
        "total_price",
        "status",
        "created_at",
    )
